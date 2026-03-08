from datetime import datetime

LOG_FILE = "data/system_log.txt"

def log_event(event):

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    log_line = f"{timestamp} | {event}\n"

    with open(LOG_FILE, "a") as file:
        file.write(log_line)
