# 🖥️ Smart Desktop Usage Analyzer

A Python + Web dashboard that tracks and analyzes desktop app usage for digital well-being.

## Features
- Tracks time spent on each app
- Generates daily usage summary
- Interactive bar chart with insights
- Web-based dashboard (HTML + Chart.js)
- Suggestions for overused apps
- Clean UI with average time/session info

## How It Works
1. `tracker.py` logs active window every 5s
2. `analyze.py` summarizes it into JSON
3. `index.html` visualizes data as chart + stats

## To Run
```bash
python tracker.py   # Let it run for a while
python analyze.py   # Summarizes and creates JSON
python -m http.server 8000  # To serve index.html
