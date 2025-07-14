import time
from datetime import datetime
import win32gui
import os

# Folder to store logs
log_folder = "logs"
os.makedirs(log_folder, exist_ok=True)

# Get today's filename
today = datetime.now().strftime("%Y-%m-%d")
log_file = os.path.join(log_folder, f"{today}_usage.txt")

# To avoid duplicate logs
last_window = ""

print("🚀 Usage Tracker Started... (Press Ctrl+C to stop)\n")

try:
    while True:
        window = win32gui.GetWindowText(win32gui.GetForegroundWindow())
        timestamp = datetime.now().strftime("%H:%M:%S")

        if window and window != last_window:
            with open(log_file, "a", encoding="utf-8") as f:
                log_line = f"[{timestamp}] - {window}\n"
                f.write(log_line)
                print(log_line.strip())
                last_window = window

        time.sleep(5)  # check every 5 seconds

except KeyboardInterrupt:
    print("\n🛑 Tracker stopped by user.")
