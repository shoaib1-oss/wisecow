#!/usr/bin/env python3
import psutil
import logging

# Configure logging
logging.basicConfig(filename="system_health.log", level=logging.INFO, format="%(asctime)s - %(message)s")

# Thresholds
CPU_THRESHOLD = 80
MEMORY_THRESHOLD = 80
DISK_THRESHOLD = 80

def check_system_health():
    alerts = []

    # CPU
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > CPU_THRESHOLD:
        alerts.append(f"High CPU Usage: {cpu_usage}%")

    # Memory
    memory = psutil.virtual_memory()
    if memory.percent > MEMORY_THRESHOLD:
        alerts.append(f"High Memory Usage: {memory.percent}%")

    # Disk
    disk = psutil.disk_usage('/')
    if disk.percent > DISK_THRESHOLD:
        alerts.append(f"High Disk Usage: {disk.percent}%")

    # Processes
    process_count = len(psutil.pids())
    alerts.append(f"Running Processes: {process_count}")

    if alerts:
        for alert in alerts:
            print(alert)
            logging.info(alert)
    else:
        print("System health is normal")
        logging.info("System health is normal")

if __name__ == "__main__":
    check_system_health()
