#!/usr/bin/env python3
"""
生成静态 JSON API 文件
输出: docs/api/v1/all.json
"""

import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))
from src.config_loader import get_enabled_sources

CDN_BASE = "https://cdn.jsdelivr.net/gh/zhboat/DailyWallpaperHub@main/docs"


def generate_api():
    wallpapers_base = Path("docs/wallpapers")
    api_dir = Path("docs/api/v1")
    api_dir.mkdir(parents=True, exist_ok=True)

    enabled_sources = get_enabled_sources()
    if not enabled_sources:
        print("[WARN] 没有启用的壁纸源")
        return

    all_wallpapers = []

    for source in enabled_sources:
        source_dir = wallpapers_base / source["name"]
        if not source_dir.exists():
            continue

        for meta_file in source_dir.rglob("meta.json"):
            date_dir = meta_file.parent
            thumb_path = date_dir / "thumb.jpg"
            image_path = date_dir / "image.jpg"

            if not (thumb_path.exists() and image_path.exists()):
                continue

            try:
                meta = json.loads(meta_file.read_text(encoding="utf-8"))
            except Exception:
                continue

            rel = date_dir.relative_to(Path("docs"))
            all_wallpapers.append({
                "date": meta.get("date", date_dir.name),
                "title": meta.get("title", date_dir.name),
                "urls": {
                    "image": f"{CDN_BASE}/{rel}/image.jpg",
                    "thumb": f"{CDN_BASE}/{rel}/thumb.jpg",
                },
            })

    all_wallpapers.sort(key=lambda x: x["date"], reverse=True)

    output = {"wallpapers": all_wallpapers}
    (api_dir / "all.json").write_text(
        json.dumps(output, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(f"[OK] docs/api/v1/all.json 已生成 ({len(all_wallpapers)} 张壁纸)")


if __name__ == "__main__":
    generate_api()
