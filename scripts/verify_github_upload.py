#!/usr/bin/env python3
import os
import sys
from pathlib import Path

# 添加项目根目录到路径
sys.path.insert(0, str(Path(__file__).parent.parent))

from src.utils import upload_to_github
from fetch_bing_wallpaper import load_env

def verify_github_upload():
    load_env() # 从 .env 加载环境变量
    
    test_file = "docs/wallpapers/unsplash/2026-01/2026-01-12/image.jpg"
    github_path = "wallpapers/unsplash/2026-01/2026-01-12/image.jpg"
    
    if not Path(test_file).exists():
        print(f"[ERROR] 测试文件不存在: {test_file}")
        return

    print(f"🚀 开始测试上传 {test_file} 到 GitHub...")
    result = upload_to_github(test_file, github_path)
    
    if result:
        print(f"✅ 上传成功! 访问地址: {result}")
    else:
        print("❌ 上传失败，请检查上面打印的错误信息。")

if __name__ == "__main__":
    verify_github_upload()
