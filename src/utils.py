#!/usr/bin/env python3
"""
企业微信群机器人推送工具
"""

import hashlib
import os
import requests
import json
import base64
import sys


def send_image_to_wecom(webhook_url: str, image_path: str):
    """
    发送图片到企业微信群机器人
    """
    with open(image_path, "rb") as f:
        image_data = f.read()
        image_base64 = base64.b64encode(image_data).decode("utf-8")
        image_md5 = hashlib.md5(image_data).hexdigest()

    payload = {
        "msgtype": "image",
        "image": {
            "base64": image_base64,
            "md5": image_md5
        }
    }

    resp = requests.post(webhook_url, json=payload, timeout=10)
    resp.raise_for_status()
    
    result = resp.json()
    if result.get("errcode") != 0:
        raise Exception(f"WeChat push failed: {result.get('errmsg')}")


def send_markdown_to_wecom(webhook_url: str, meta: dict, source_name: str = "Bing"):
    """
    发送 Markdown 消息到企业微信群机器人
    """
    title = meta.get("title", "")
    copyright_info = meta.get("copyright", "")
    date = meta.get("date", "")

    content = f"""### 🖼 今日{source_name}壁纸 · {date}

**{title}**

> {copyright_info}

📦 已自动归档至 [GitHub 仓库](https://github.com/Hana19951208/DailyWallpaperHub)
🔁 自动化定时任务运行中"""

    payload = {
        "msgtype": "markdown",
        "markdown": {
            "content": content
        }
    }

    resp = requests.post(webhook_url, json=payload, timeout=10)
    resp.raise_for_status()
    
    result = resp.json()
    if result.get("errcode") != 0:
        raise Exception(f"WeChat push failed: {result.get('errmsg')}")


def send_story_to_wecom(webhook_url: str, meta: dict, story_content: str):
    """
    推送壁纸故事到企业微信（Markdown 格式）
    """
    try:
        title = meta.get("title", "每日壁纸")
        date = meta.get("date", "")
        
        # 构建 Markdown 内容
        # 移除任何形式的图片引用 (Markdown 格式: ![alt](url))
        import re
        story_text = re.sub(r'!\[.*?\]\(.*?\)', '', story_content).strip()
        
        # 限制长度（企业微信限制 2048 字节）
        max_length = 1800 
        if len(story_text.encode('utf-8')) > max_length:
            content_bytes = story_text.encode('utf-8')[:max_length]
            story_text = content_bytes.decode('utf-8', errors='ignore') + "\n\n...\n\n> 查看完整故事请访问 GitHub 仓库"
        
        markdown_text = f"# 📖 {title}\n\n**日期**: {date}\n\n---\n\n{story_text}"
        
        payload = {
            "msgtype": "markdown",
            "markdown": {
                "content": markdown_text
            }
        }
        
        resp = requests.post(webhook_url, json=payload, timeout=10)
        resp.raise_for_status()
        result = resp.json()
        
        if result.get("errcode") != 0:
            print(f"[WARN] 企业微信故事推送返回错误: {result.get('errmsg')}")
    except Exception as e:
        print(f"[ERROR] 企业微信故事推送失败: {e}")


def upload_to_github(local_path: str, github_path: str):
    """
    上传文件到指定的 GitHub 仓库（替代 COS）
    """
    token = os.environ.get('GH_PAT') or os.environ.get('GITHUB_TOKEN')
    repo = os.environ.get('IMAGE_REPO', 'Hana19951208/blog-images')
    branch = os.environ.get('IMAGE_REPO_BRANCH', 'main')

    if not token:
        print("[INFO] GH_PAT/GITHUB_TOKEN 未配置，跳过 GitHub 上传")
        return None

    try:
        # 读取文件内容并进行 base64 编码
        with open(local_path, "rb") as f:
            content = base64.b64encode(f.read()).decode("utf-8")

        # GitHub API URL
        url = f"https://api.github.com/repos/{repo}/contents/{github_path}"
        
        headers = {
            "Authorization": f"token {token}",
            "Accept": "application/vnd.github.v3+json"
        }

        # 检查文件是否已存在（为了获取 sha 以进行更新）
        sha = None
        resp = requests.get(url, headers=headers)
        if resp.status_code == 200:
            sha = resp.json().get("sha")
            print(f"[INFO] 文件已存在，准备更新: {github_path}")

        # 提交更改
        payload = {
            "message": f"upload: {github_path} (auto sync)",
            "content": content,
            "branch": branch
        }
        if sha:
            payload["sha"] = sha

        put_resp = requests.put(url, headers=headers, json=payload)
        put_resp.raise_for_status()
        
        raw_url = f"https://raw.githubusercontent.com/{repo}/{branch}/{github_path}"
        print(f"[OK] 文件已同步至 GitHub: {raw_url}")
        return raw_url
    except Exception as e:
        print(f"[ERROR] GitHub 上传失败: {e}")
        return None
