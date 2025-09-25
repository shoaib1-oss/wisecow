import psutil
import time

# Define thresholds
CPU_THRESHOLD = 80  # percent
MEMORY_THRESHOLD = 80  # percent
DISK_THRESHOLD = 80  # percent

LOG_FILE = "system_health.log"

def log_message(message):
    """Write message to log file with timestamp."""
    with open(LOG_FILE, "a") as log:
        log.write(f"{time.strftime('%Y-%m-%d %H:%M:%S')} - {message}\n")

def check_system_health():
    """Check CPU, Memory, Disk, and Processes."""
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent

    log_message(f"CPU: {cpu}% | Memory: {memory}% | Disk: {disk}%")

    if cpu > CPU_THRESHOLD:
        log_message(f"ALERT: CPU usage high at {cpu}%")
    if memory > MEMORY_THRESHOLD:
        log_message(f"ALERT: Memory usage high at {memory}%")
    if disk > DISK_THRESHOLD:
        log_message(f"ALERT: Disk usage high at {disk}%")

    processes = len(psutil.pids())
    log_message(f"Running processes: {processes}")

if __name__ == "__main__":
    while True:
        check_system_health()
        time.sleep(10)  # check every 10 seconds
