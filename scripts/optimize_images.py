#!/usr/bin/env python3
"""
图片优化工具：
1. 批量压缩存量图片
2. 提供给抓取脚本调用的压缩接口
"""

import os
import subprocess
from pathlib import Path

def compress_image(image_path: Path, target_size_kb: int = 400):
    """
    使用 jpegoptim 压缩单张图片
    """
    if not image_path.exists():
        print(f"[ERROR] 文件不存在: {image_path}")
        return False
    
    if image_path.suffix.lower() not in ['.jpg', '.jpeg']:
        print(f"[INFO] 跳过非 JPG 文件: {image_path}")
        return False

    print(f">>> [压缩中] {image_path} (目标: {target_size_kb}k)")
    try:
        # 尝试调用 jpegoptim
        # --size 指定目标大小，--strip-all 移除所有元数据（减小体积）
        subprocess.run(
            ['jpegoptim', f'--size={target_size_kb}k', '--strip-all', str(image_path)],
            check=True,
            capture_output=True
        )
        return True
    except FileNotFoundError:
        print("[ERROR] 系统未安装 jpegoptim，请先安装：sudo apt-get install jpegoptim")
        return False
    except subprocess.CalledProcessError as e:
        print(f"[ERROR] 压缩失败: {e}")
        return False

def batch_optimize_legacy():
    """
    遍历 docs/wallpapers 优化所有存量图片
    """
    print("🚀 开始扫描存量图片进行优化...")
    base_dir = Path("docs/wallpapers")
    if not base_dir.exists():
        print("[ERROR] 目录不存在")
        return

    count = 0
    # 递归搜索所有 image.jpg
    for img_path in base_dir.rglob("image.jpg"):
        original_size = img_path.stat().st_size / 1024
        if original_size > 450: # 稍微留一点余量，大于 450k 的才处理
            if compress_image(img_path):
                new_size = img_path.stat().st_size / 1024
                print(f"  ✅ 优化完成: {original_size:.1f}k -> {new_size:.1f}k")
                count += 1
        else:
            print(f"  [跳过] {img_path.relative_to(base_dir)} 大小合适 ({original_size:.1f}k)")

    print(f"\n✨ 存量优化脚本运行结束，共处理 {count} 张图片。")

if __name__ == "__main__":
    # 如果系统安装了 jpegoptim 则运行
    batch_optimize_legacy()
