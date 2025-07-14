import os
import json
from datetime import datetime
from collections import defaultdict

# Folder where logs are stored
log_folder = "logs"
today = datetime.now().strftime("%Y-%m-%d")
log_file = os.path.join(log_folder, f"{today}_usage.txt")

# Check for log file
if not os.path.exists(log_file):
    print("❌ No log file found for today.")
    exit()

# Read usage log
usage = []
with open(log_file, "r", encoding="utf-8") as f:
    for line in f:
        try:
            timestamp_str, window = line.strip().split("] - ")
            timestamp = datetime.strptime(timestamp_str[1:], "%H:%M:%S")
            usage.append((timestamp, window))
        except Exception:
            continue

# Estimate time spent per app
usage_by_window = defaultdict(int)
for i in range(len(usage) - 1):
    current_time, current_window = usage[i]
    next_time, _ = usage[i + 1]
    duration = int((next_time - current_time).total_seconds())
    if 0 <= duration <= 3600:
        usage_by_window[current_window] += duration

# Add default 5s for last app
if usage:
    last_window = usage[-1][1]
    usage_by_window[last_window] += 5

# Sort usage data
sorted_usage = sorted(usage_by_window.items(), key=lambda x: -x[1])

# Display summary in console
print(f"\n📊 App Usage Summary for {today}:\n")
total_time = 0
for window, seconds in sorted_usage:
    minutes = seconds // 60
    print(f"🔸 {window[:40]:40} → {minutes} min")
    total_time += seconds

print(f"\n⏳ Total time tracked: {total_time // 60} minutes")

# Suggest overused app
suggestion = None
if sorted_usage:
    top_app, top_time = sorted_usage[0]
    if top_time > 90 * 60:
        suggestion = f"⚠️ You spent too much time on: {top_app}"
        print(f"\n{suggestion}")
    else:
        suggestion = "✅ Good control — no overused apps detected today."
        print(f"\n{suggestion}")

# Export summary to JSON
summary_data = {
    "date": today,
    "total_minutes": total_time // 60,
    "apps": [
        {"app": window, "minutes": seconds // 60}
        for window, seconds in sorted_usage
    ],
    "suggestion": suggestion
}

summary_file = os.path.join(log_folder, f"{today}_summary.json")
with open(summary_file, "w", encoding="utf-8") as f:
    json.dump(summary_data, f, indent=2)

print(f"\n✅ Summary saved to: {summary_file}")
