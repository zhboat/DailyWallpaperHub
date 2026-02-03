#!/usr/bin/env python3
"""
音频推送独立脚本 (Standalone Version)
功能：将本地音频/文件推送到企业微信。如果文件超过 20MB，自动转存至 GitHub 并发送链接。
"""

import os
import sys
import json
import base64
import re
import requests
import datetime
import argparse

# ==========================================
# 核心配置 (优先读取环境变量/.env，其次使用默认值)
# ==========================================
WEWORK_WEBHOOK = os.environ.get("WEWORK_WEBHOOK", "")
GH_PAT = os.environ.get("GH_PAT", "")
IMAGE_REPO = os.environ.get("IMAGE_REPO", "Hana19951208/blog-images")
IMAGE_REPO_BRANCH = os.environ.get("IMAGE_REPO_BRANCH", "main")

# 企业微信文件大小限制 (20MB)
WECOM_FILE_LIMIT_MB = 20

def load_env_simple(env_path=".env"):
    """
    简单的 .env 文件解析器，支持独立运行
    """
    if not os.path.exists(env_path):
        return
    with open(env_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith('#'):
                continue
            if '=' in line:
                key, value = line.split('=', 1)
                key = key.strip()
                value = value.strip().strip("'").strip('"')
                os.environ[key] = value

def upload_to_github(local_path: str, github_path: str):
    """
    上传文件到指定的 GitHub 仓库
    """
    token = os.environ.get('GH_PAT') or os.environ.get('GITHUB_TOKEN')
    repo = os.environ.get('IMAGE_REPO', IMAGE_REPO)
    branch = os.environ.get('IMAGE_REPO_BRANCH', IMAGE_REPO_BRANCH)

    if not token:
        print("[WARN] 未配置 GitHub Token，无法上传大文件")
        return None

    try:
        with open(local_path, "rb") as f:
            content = base64.b64encode(f.read()).decode("utf-8")

        url = f"https://api.github.com/repos/{repo}/contents/{github_path}"
        headers = {
            "Authorization": f"token {token}",
            "Accept": "application/vnd.github.v3+json",
            "User-Agent": "Standalone-Push-Bot"
        }

        # 检查文件是否已存在以获取 SHA
        sha = None
        resp = requests.get(url, headers=headers)
        if resp.status_code == 200:
            sha = resp.json().get("sha")
        
        payload = {
            "message": f"upload: {os.path.basename(github_path)} (standalone push)",
            "content": content,
            "branch": branch
        }
        if sha:
            payload["sha"] = sha

        put_resp = requests.put(url, headers=headers, json=payload)
        if put_resp.status_code in [200, 201]:
            return f"https://raw.githubusercontent.com/{repo}/{branch}/{github_path}"
        else:
            print(f"[ERROR] GitHub API 错误: {put_resp.text}")
            return None
    except Exception as e:
        print(f"[ERROR] GitHub 上传异常: {e}")
        return None

def send_file_to_wecom(webhook_url: str, file_path: str):
    """
    发送本地文件到企业微信群机器人 (≤ 20MB)
    """
    match = re.search(r'key=([a-z0-9-]+)', webhook_url)
    if not match:
        raise Exception("Webhook URL 格式不正确，未发现 key")
    
    key = match.group(1)
    
    # 1. 上传文件获取 media_id
    upload_url = f"https://qyapi.weixin.qq.com/cgi-bin/webhook/upload_media?key={key}&type=file"
    file_name = os.path.basename(file_path)
    
    with open(file_path, 'rb') as f:
        files = {'file': (file_name, f)}
        resp = requests.post(upload_url, files=files, timeout=60)
        resp.raise_for_status()
        res = resp.json()
        
        if res.get('errcode') != 0:
            raise Exception(f"素材上传失败: {res.get('errmsg')}")
        
        media_id = res.get('media_id')

    # 2. 发送消息
    payload = {
        "msgtype": "file",
        "file": {"media_id": media_id}
    }
    
    send_resp = requests.post(webhook_url, json=payload, timeout=10)
    send_res = send_resp.json()
    if send_res.get('errcode') != 0:
        raise Exception(f"消息发送失败: {send_res.get('errmsg')}")
    
    print(f"[OK] 文件 '{file_name}' 已直接推送")

def main():
    parser = argparse.ArgumentParser(description="Standalone Audio/File Pusher for WeChat")
    parser.add_argument("file", help="本地文件完整路径")
    parser.add_argument("--webhook", help="覆盖 WEWORK_WEBHOOK 环境变量")
    args = parser.parse_args()

    # 1. 环境准备
    # 尝试在脚本所在目录或当前目录寻找 .env
    load_env_simple(os.path.join(os.path.dirname(__file__), '.env'))
    load_env_simple() 
    
    webhook_url = args.webhook or os.environ.get("WEWORK_WEBHOOK")
    if not webhook_url:
        print("[ERROR] 缺失 Webhook 地址。请在 .env 中配置或使用 --webhook 参数")
        return

    file_path = args.file
    if not os.path.exists(file_path):
        print(f"[ERROR] 文件未找到: {file_path}")
        return

    # 2. 逻辑分流
    file_size_mb = os.path.getsize(file_path) / (1024 * 1024)
    file_name = os.path.basename(file_path)
    
    print(f"🚀 处理文件: {file_name} ({file_size_mb:.2f}MB)")

    if file_size_mb <= WECOM_FILE_LIMIT_MB:
        try:
            send_file_to_wecom(webhook_url, file_path)
        except Exception as e:
            print(f"❌ 推送失败: {e}")
    else:
        print(f"[INFO] 文件超出 20MB，启动 GitHub 转存...")
        # 存放在 GitHub 的相对路径
        github_path = f"archives/audio/{file_name}"
        raw_url = upload_to_github(file_path, github_path)
        
        if raw_url:
            date_str = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            content = (
                f"### 🎙️ 音频文件转存提醒\n\n"
                f"**文件名**: {file_name}\n"
                f"**大小**: {file_size_mb:.2f} MB\n"
                f"**状态**: 自动转存至 GitHub (超出 WeCom 限制)\n"
                f"**时间**: {date_str}\n\n"
                f"🔗 [点击下载/点播音频]({raw_url})"
            )
            
            payload = {
                "msgtype": "markdown",
                "markdown": {"content": content}
            }
            resp = requests.post(webhook_url, json=payload, timeout=10)
            if resp.json().get("errcode") == 0:
                print(f"[SUCCESS] 链接已推送至企业微信")
            else:
                print(f"[ERROR] 消息推送失败: {resp.text}")
        else:
            print(f"[ERROR] GitHub 链路执行失败")

if __name__ == "__main__":
    main()
