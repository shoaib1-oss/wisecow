import psutil
import time
import logging

# Setup logging (to file and console)
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler("system_health.log"),
        logging.StreamHandler()  # this prints to console
    ]
)

# Thresholds
CPU_THRESHOLD = 80
MEMORY_THRESHOLD = 80
DISK_THRESHOLD = 80

def check_system_health():
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent

    logging.info(f"CPU: {cpu}%, Memory: {memory}%, Disk: {disk}%")

    if cpu > CPU_THRESHOLD:
        logging.warning(f"High CPU Usage: {cpu}%")
    if memory > MEMORY_THRESHOLD:
        logging.warning(f"High Memory Usage: {memory}%")
    if disk > DISK_THRESHOLD:
        logging.warning(f"High Disk Usage: {disk}%")

if __name__ == "__main__":
    while True:
        check_system_health()
        time.sleep(10)
