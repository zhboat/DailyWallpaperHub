#!/usr/bin/env python3
"""
生成静态 JSON API 文件（增量更新）
输出: docs/api/v1/all.json
"""

import json
import sys
from pathlib import Path
from PIL import Image

sys.path.insert(0, str(Path(__file__).parent.parent))
from src.config_loader import get_enabled_sources

CDN_BASE = "https://cdn.jsdelivr.net/gh/zhboat/DailyWallpaperHub@main/docs"


def generate_api():
    wallpapers_base = Path("docs/wallpapers")
    api_dir = Path("docs/api/v1")
    api_dir.mkdir(parents=True, exist_ok=True)
    api_file = api_dir / "all.json"

    enabled_sources = get_enabled_sources()
    if not enabled_sources:
        print("[WARN] 没有启用的壁纸源")
        return

    # 加载已有数据，用 image URL 作为去重 key
    existing = {}
    if api_file.exists():
        try:
            data = json.loads(api_file.read_text(encoding="utf-8"))
            for wp in data.get("wallpapers", []):
                existing[wp["image"]] = wp
        except Exception:
            pass

    new_count = 0
    for source in enabled_sources:
        source_dir = wallpapers_base / source["name"]
        if not source_dir.exists():
            continue

        for meta_file in source_dir.rglob("meta.json"):
            date_dir = meta_file.parent
            image_path = date_dir / "image.jpg"
            thumb_path = date_dir / "thumb.jpg"

            if not (thumb_path.exists() and image_path.exists()):
                continue

            rel = date_dir.relative_to(Path("docs"))
            image_url = f"{CDN_BASE}/{rel}/image.jpg"

            # 已存在则跳过
            if image_url in existing:
                continue

            try:
                meta = json.loads(meta_file.read_text(encoding="utf-8"))
            except Exception:
                continue

            with Image.open(image_path) as img:
                width, height = img.size

            existing[image_url] = {
                "date": meta.get("date", date_dir.name),
                "title": meta.get("title", date_dir.name),
                "source": source["name"],
                "fileSize": image_path.stat().st_size,
                "resolution": f"{width}x{height}",
                "image": image_url,
                "thumb": f"{CDN_BASE}/{rel}/thumb.jpg",
            }
            new_count += 1

    all_wallpapers = sorted(existing.values(), key=lambda x: x["date"], reverse=True)

    output = {"wallpapers": all_wallpapers}
    api_file.write_text(
        json.dumps(output, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(f"[OK] docs/api/v1/all.json 已更新 (共 {len(all_wallpapers)} 张, 新增 {new_count} 张)")


if __name__ == "__main__":
    generate_api()
