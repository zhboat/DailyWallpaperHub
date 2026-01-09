# 📅 DailyWallpaperHub

> Multi-source Wallpaper Aggregator · Auto-archive Bing + Unsplash · AI Visual Story Generation · WeChat Push · GitHub Pages Gallery

[English](README_EN.md) | [中文](README.md)

[![Daily Update](https://github.com/Hana19951208/DailyWallpaperHub/actions/workflows/daily.yml/badge.svg)](https://github.com/Hana19951208/DailyWallpaperHub/actions/workflows/daily.yml)
[![Pages](https://img.shields.io/badge/GitHub%20Pages-Online-brightgreen)](https://Hana19951208.github.io/DailyWallpaperHub/)

---

## ✨ Features

- **🎨 Multi-Source Aggregation**: Supports multiple wallpaper sources like Bing and Unsplash. Configurable and easy to extend.
- **⚡️ Async Architecture**: AI story generation runs asynchronously. Main process is fast, making images available immediately.
- **🤖 AI Visual Stories**: Integrated with LLM visual models to auto-generate exquisite cultural stories (approx. 500 words) for each wallpaper.
- **📝 Externalized Prompts**: AI prompts stored in `prompts/story_prompt.txt` for easy customization.
- **⏰ Smart Scheduling**: GitHub Actions checks for updates every hour to get the latest wallpapers ASAP.
- **💾 Persistent Archiving**: High-res images, thumbnails, metadata (JSON), and AI stories are auto-committed to the repo, never lost.
- **🎭 Modern Gallery**: Built-in GitHub Pages gallery with responsive design and dark mode.
- **📱 WeChat Push**: Automatically pushes images, metadata, and AI stories to Enterprise WeChat groups (Markdown supported).
- **🎯 Quantity Limit**: Default index shows only the last 10 days to avoid clutter (adjustable in `config/sources.yaml`).
- **🛠 Batch Tools**: Supports batch fetching of historical wallpapers by date and source.
- **💰 Zero Cost**: Built entirely on free GitHub resources.

---

## 🖼 Showcase

### Online Gallery

![Gallery Screenshot](docs/preview.png)

### AI Stories (Click Title to Read)
Click the title in the wallpaper index to jump to the AI-generated background story (includes original image display).

---

## 📅 Wallpaper Index (Latest)

<!-- WALLPAPER_INDEX_START -->
<table width="100%">
<tr><th width="15%">日期</th><th width="42%">Bing 🔍</th><th width="42%">Unsplash 📷</th></tr>
<tr>
<td align="center"><b>2026-01-09</b></td>
<td align="center" valign="top"><a href="docs/wallpapers/bing/2026-01/2026-01-09/image.jpg"><img src="docs/wallpapers/bing/2026-01/2026-01-09/thumb.jpg" width="100%" style="border-radius:10px;"></a><br /><a href="docs/wallpapers/bing/2026-01/2026-01-09/story.md"><small>当节日的魔法踩着蹄声而来 📖</small></a></td>
<td align="center" valign="top"><a href="docs/wallpapers/unsplash/2026-01/2026-01-09/image.jpg"><img src="docs/wallpapers/unsplash/2026-01/2026-01-09/thumb.jpg" width="100%" style="border-radius:10px;"></a><br /><a href="docs/wallpapers/unsplash/2026-01/2026-01-09/story.md"><small>a view of a mountain range from a plane 📖</small></a></td>
</tr>
<tr>
<td align="center"><b>2026-01-08</b></td>
<td align="center" valign="top"><a href="docs/wallpapers/bing/2026-01/2026-01-08/image.jpg"><img src="docs/wallpapers/bing/2026-01/2026-01-08/thumb.jpg" width="100%" style="border-radius:10px;"></a><br /><a href="docs/wallpapers/bing/2026-01/2026-01-08/story.md"><small>时光在此处茁壮成长 📖</small></a></td>
<td align="center" valign="top"><a href="docs/wallpapers/unsplash/2026-01/2026-01-08/image.jpg"><img src="docs/wallpapers/unsplash/2026-01/2026-01-08/thumb.jpg" width="100%" style="border-radius:10px;"></a><br /><a href="docs/wallpapers/unsplash/2026-01/2026-01-08/story.md"><small>brown concrete building near green trees under cloudy sky during daytime 📖</small></a></td>
</tr>
<tr>
<td align="center"><b>2026-01-07</b></td>
<td align="center" valign="top"><a href="docs/wallpapers/bing/2026-01/2026-01-07/image.jpg"><img src="docs/wallpapers/bing/2026-01/2026-01-07/thumb.jpg" width="100%" style="border-radius:10px;"></a><br /><a href="docs/wallpapers/bing/2026-01/2026-01-07/story.md"><small>废墟之上，椋鸟群舞 📖</small></a></td>
<td align="center" valign="top"><a href="docs/wallpapers/unsplash/2026-01/2026-01-07/image.jpg"><img src="docs/wallpapers/unsplash/2026-01/2026-01-07/thumb.jpg" width="100%" style="border-radius:10px;"></a><br /><a href="docs/wallpapers/unsplash/2026-01/2026-01-07/story.md"><small>green trees on brown mountain near body of water during daytime 📖</small></a></td>
</tr>
<tr>
<td align="center"><b>2026-01-06</b></td>
<td align="center" valign="top"><a href="docs/wallpapers/bing/2026-01/2026-01-06/image.jpg"><img src="docs/wallpapers/bing/2026-01/2026-01-06/thumb.jpg" width="100%" style="border-radius:10px;"></a><br /><a href="docs/wallpapers/bing/2026-01/2026-01-06/story.md"><small>古老岩石的传奇 📖</small></a></td>
<td align="center" valign="top"><a href="docs/wallpapers/unsplash/2026-01/2026-01-06/image.jpg"><img src="docs/wallpapers/unsplash/2026-01/2026-01-06/thumb.jpg" width="100%" style="border-radius:10px;"></a><br /><small>a house in the middle of a mountain range</small></td>
</tr>
<tr>
<td align="center"><b>2026-01-05</b></td>
<td align="center" valign="top"><a href="docs/wallpapers/bing/2026-01/2026-01-05/image.jpg"><img src="docs/wallpapers/bing/2026-01/2026-01-05/thumb.jpg" width="100%" style="border-radius:10px;"></a><br /><a href="docs/wallpapers/bing/2026-01/2026-01-05/story.md"><small>努克的慵懒时光 📖</small></a></td>
<td align="center" valign="top"><a href="docs/wallpapers/unsplash/2026-01/2026-01-05/image.jpg"><img src="docs/wallpapers/unsplash/2026-01/2026-01-05/thumb.jpg" width="100%" style="border-radius:10px;"></a><br /><a href="docs/wallpapers/unsplash/2026-01/2026-01-05/story.md"><small>white and brown house near body of water during daytime 📖</small></a></td>
</tr>
<tr>
<td align="center"><b>2026-01-04</b></td>
<td align="center" valign="top"><a href="docs/wallpapers/bing/2026-01/2026-01-04/image.jpg"><img src="docs/wallpapers/bing/2026-01/2026-01-04/thumb.jpg" width="100%" style="border-radius:10px;"></a><br /><a href="docs/wallpapers/bing/2026-01/2026-01-04/story.md"><small>高角羚群紧急戒备 📖</small></a></td>
<td align="center" valign="top"><a href="docs/wallpapers/unsplash/2026-01/2026-01-04/image.jpg"><img src="docs/wallpapers/unsplash/2026-01/2026-01-04/thumb.jpg" width="100%" style="border-radius:10px;"></a><br /><a href="docs/wallpapers/unsplash/2026-01/2026-01-04/story.md"><small>snow covered mountain under starry night 📖</small></a></td>
</tr>
<tr>
<td align="center"><b>2026-01-03</b></td>
<td align="center" valign="top"><a href="docs/wallpapers/bing/2026-01/2026-01-03/image.jpg"><img src="docs/wallpapers/bing/2026-01/2026-01-03/thumb.jpg" width="100%" style="border-radius:10px;"></a><br /><a href="docs/wallpapers/bing/2026-01/2026-01-03/story.md"><small>王者视野 📖</small></a></td>
<td align="center" valign="top"><a href="docs/wallpapers/unsplash/2026-01/2026-01-03/image.jpg"><img src="docs/wallpapers/unsplash/2026-01/2026-01-03/thumb.jpg" width="100%" style="border-radius:10px;"></a><br /><a href="docs/wallpapers/unsplash/2026-01/2026-01-03/story.md"><small>Nature trail surrounded by trees.  📖</small></a></td>
</tr>
<tr>
<td align="center"><b>2026-01-02</b></td>
<td align="center" valign="top"><a href="docs/wallpapers/bing/2026-01/2026-01-02/image.jpg"><img src="docs/wallpapers/bing/2026-01/2026-01-02/thumb.jpg" width="100%" style="border-radius:10px;"></a><br /><a href="docs/wallpapers/bing/2026-01/2026-01-02/story.md"><small>传奇故事前的篇章 📖</small></a></td>
<td align="center" valign="top"><a href="docs/wallpapers/unsplash/2026-01/2026-01-02/image.jpg"><img src="docs/wallpapers/unsplash/2026-01/2026-01-02/thumb.jpg" width="100%" style="border-radius:10px;"></a><br /><a href="docs/wallpapers/unsplash/2026-01/2026-01-02/story.md"><small>A dirt road in front of a snow covered mountain 📖</small></a></td>
</tr>
<tr>
<td align="center"><b>2026-01-01</b></td>
<td align="center" valign="top"><a href="docs/wallpapers/bing/2026-01/2026-01-01/image.jpg"><img src="docs/wallpapers/bing/2026-01/2026-01-01/thumb.jpg" width="100%" style="border-radius:10px;"></a><br /><a href="docs/wallpapers/bing/2026-01/2026-01-01/story.md"><small>威尼斯的灵魂 📖</small></a></td>
<td align="center" valign="top"><a href="docs/wallpapers/unsplash/2026-01/2026-01-01/image.jpg"><img src="docs/wallpapers/unsplash/2026-01/2026-01-01/thumb.jpg" width="100%" style="border-radius:10px;"></a><br /><a href="docs/wallpapers/unsplash/2026-01/2026-01-01/story.md"><small>a view of the mountains from the top of a hill 📖</small></a></td>
</tr>
<tr>
<td align="center"><b>2025-12-31</b></td>
<td align="center" valign="top"><a href="docs/wallpapers/bing/2025-12/2025-12-31/image.jpg"><img src="docs/wallpapers/bing/2025-12/2025-12-31/thumb.jpg" width="100%" style="border-radius:10px;"></a><br /><a href="docs/wallpapers/bing/2025-12/2025-12-31/story.md"><small>伸个懒腰，迈向新年！ 📖</small></a></td>
<td align="center" valign="top"><a href="docs/wallpapers/unsplash/2025-12/2025-12-31/image.jpg"><img src="docs/wallpapers/unsplash/2025-12/2025-12-31/thumb.jpg" width="100%" style="border-radius:10px;"></a><br /><a href="docs/wallpapers/unsplash/2025-12/2025-12-31/story.md"><small>gray concrete bridge over river under cloudy sky during daytime 📖</small></a></td>
</tr>
</table>
<!-- WALLPAPER_INDEX_END -->

---

## 🚀 Quick Start

### Local Development

```bash
# 1. Clone repository
git clone https://github.com/Hana19951208/DailyWallpaperHub.git
cd DailyWallpaperHub

# 2. Install dependencies (using conda env)
conda activate base
pip install -r requirements.txt

# 3. Configure Environment Variables
cp .env.example .env
# Edit .env file with your configurations:
# WEWORK_WEBHOOK=your_webhook_url
# LLM_API_KEY=your_api_key
# LLM_BASE_URL=https://api.openai.com/v1
# LLM_MODEL_NAME=gpt-4o
# UNSPLASH_ACCESS_KEY=your_unsplash_key

# 4. Fast Fetch (Skip Story)
python fetch_bing_wallpaper.py --skip-story
python fetch_unsplash_wallpaper.py --skip-story

# 5. Async Story Generation (Background)
python scripts/generate_missing_stories.py

# 6. Batch Fetch History
python batch_fetch.py bing 2025-12        # Fetch Bing whole month
python batch_fetch.py unsplash 2025-12-10 # Fetch Unsplash specific date
```

### GitHub Actions Deployment

1. **Fork this repository**

2. **Configure GitHub Secrets** (Settings → Secrets and variables → Actions):
   - `WEWORK_WEBHOOK`: Enterprise WeChat Robot Webhook URL
   - `LLM_API_KEY`: LLM API Key
   - `LLM_BASE_URL`: LLM API Base URL
   - `LLM_MODEL_NAME`: LLM Model Name
   - `UNSPLASH_ACCESS_KEY`: Unsplash API Access Key

3. **Enable GitHub Pages**:
   - Settings → Pages
   - Source: Deploy from a branch
   - Branch: `main` / `docs`

4. **Trigger manually or wait for schedule**:
   - Actions → Daily Wallpaper Fetch → Run workflow

---

## 📁 Project Structure

```
DailyWallpaperHub/
├── config/
│   └── sources.yaml          # Data Source Config
├── prompts/
│   └── story_prompt.txt      # AI Prompt Template
├── scripts/
│   ├── fill_unsplash_dec.py  # Unsplash Data Fill Script
│   └── generate_missing_stories.py  # Async Story Gen Script
├── src/
│   ├── config_loader.py      # Config Loader
│   ├── utils.py              # WeChat Push Utils
│   ├── update_readme.py      # README Updater
│   └── update_gallery.py     # Gallery Updater
├── docs/
│   ├── index.html            # GitHub Pages Gallery
│   └── wallpapers/           # 404 Fix: Wallpapers must be here for Pages
│       ├── bing/
│       │   └── YYYY-MM-DD/
│       │       ├── image.jpg
│       │       ├── thumb.jpg
│       │       ├── meta.json
│       │       └── story.md
│       └── unsplash/
│           └── YYYY-MM-DD/
│               ├── image.jpg
│               ├── thumb.jpg
│               ├── meta.json
│               └── story.md
├── .github/workflows/
│   └── daily.yml             # Automation Workflow
├── fetch_bing_wallpaper.py   # Bing Fetcher
├── fetch_unsplash_wallpaper.py # Unsplash Fetcher
├── batch_fetch.py            # Batch Tool
├── requirements.txt          # Python Dependencies
└── README.md                 # Documentation
```

---

## 🎯 Usage Guide

### Async Story Generation

To improve user experience, this project uses an asynchronous architecture:

1. **Fast Mode** (Default/Recommended):
   ```bash
   python fetch_bing_wallpaper.py --skip-story
   ```
   - Downloads images and metadata only
   - Immediately updates README and Gallery
   - Images viewable instantly

2. **Background Story Generation**:
   ```bash
   python scripts/generate_missing_stories.py
   ```
   - Scans for wallpapers missing stories
   - Batch calls LLM to generate stories
   - Auto-updates metadata and pages

### Batch Fetching

```bash
# Fetch Bing Wallpapers
python batch_fetch.py bing 2025-12        # Whole Month
python batch_fetch.py bing 2025-12-10     # Specific Date

# Fetch Unsplash Wallpapers
python batch_fetch.py unsplash 2025-12    # Whole Month (Multiple Featured)
python batch_fetch.py unsplash 2025-12-10 # Specific Date

# Source Case Insensitive
python batch_fetch.py BING 2025-12
python batch_fetch.py Unsplash 2025-12-10
```

### Adding New Sources

1. Edit `config/sources.yaml`:
   ```yaml
   sources:
     - name: new_source
       display_name: "New Source 🎨"
       enabled: true
       api_key_env: "NEW_SOURCE_API_KEY"
       fetcher_script: "fetch_new_source.py"
   ```

2. Create `fetch_new_source.py` fetcher script

3. Run tests and commit

---

## 🤝 Follow Me

<img src="docs/wechat.jpg" width="200" alt="WeChat Official Account">

> Scan to follow "Knowledge into System" (把知识变成系统)

## ⚖️ License

MIT License. For learning and exchange only. Wallpaper copyrights belong to Bing and Unsplash.
