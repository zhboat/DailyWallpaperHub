#!/usr/bin/env python3
import os
import shutil
from pathlib import Path

def migrate_folders():
    base_path = Path("docs/wallpapers")
    sources = ["bing", "unsplash"]
    
    for source in sources:
        source_dir = base_path / source
        if not source_dir.exists():
            continue
            
        print(f"Processing source: {source}")
        
        # 遍历所有日期格式的文件夹 YYYY-MM-DD
        for item in source_dir.iterdir():
            if item.is_dir() and len(item.name) == 10 and item.name.startswith("20"):
                date_str = item.name
                month_str = date_str[:7] # YYYY-MM
                
                target_month_dir = source_dir / month_str
                target_month_dir.mkdir(parents=True, exist_ok=True)
                
                target_path = target_month_dir / date_str
                
                if target_path.exists():
                    print(f"  [SKIP] {date_str} already exists in {month_str}")
                    # 如果目标已经存在，可能需要合并或删除旧的。这里保险起见先跳过或重命名
                    continue
                
                print(f"  [MOVE] {date_str} -> {month_str}/{date_str}")
                shutil.move(str(item), str(target_path))

if __name__ == "__main__":
    migrate_folders()
