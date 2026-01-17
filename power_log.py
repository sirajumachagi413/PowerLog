import csv
import random
import time
import os
from datetime import datetime

# Configuration
LOG_FILE = "power_data_py.csv" # Renamed to avoid conflict if running both
INTERVAL = 1  # Seconds

def get_reading():
    """Simulates reading from a hardware sensor."""
    # Simulate normal voltage 220-240V with occasional spikes
    base_voltage = 230
    noise = random.uniform(-10, 10)
    
    # Randomly inject a fault event (10% chance)
    if random.random() < 0.1:
        noise += random.choice([20, -25]) # Surge or Brownout

    voltage = base_voltage + noise
    
    # Simulate current varying with load
    current = random.uniform(5.0, 15.0)
    
    power = voltage * current
    return voltage, current, power

def determine_status(voltage):
    if voltage > 245:
        return "SURGE WARNING"
    elif voltage < 210:
        return "BROWNOUT WARNING"
    else:
        return "NORMAL"

def init_csv():
    """Creates the CSV file with headers if it doesn't exist."""
    if not os.path.exists(LOG_FILE):
        with open(LOG_FILE, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(["Timestamp", "Voltage (V)", "Current (A)", "Power (W)", "Status"])

def log_data(voltage, current, power, status):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Write to File
    with open(LOG_FILE, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([timestamp, round(voltage, 1), round(current, 2), round(power, 1), status])
    
    return timestamp

def main():
    init_csv()
    print("============================================")
    print("   PowerLog - Infrastructure Monitor (Py)   ")
    print("============================================")
    print(f"Monitoring started. Logging to {LOG_FILE}...\n")
    print(f"{'TIMESTAMP':<22} {'VOLT(V)':<10} {'CURR(A)':<10} {'PWR(W)':<10} {'STATUS'}")
    print("-" * 65)

    try:
        while True:
            voltage, current, power = get_reading()
            status = determine_status(voltage)
            timestamp = log_data(voltage, current, power, status)

            # Color output for warnings (using ANSI codes)
            color = "\033[91m" if status != "NORMAL" else "\033[0m" # Red for alert
            reset = "\033[0m"
            
            print(f"{color}{timestamp:<22} {voltage:<10.1f} {current:<10.2f} {power:<10.1f} {status}{reset}")
            
            time.sleep(INTERVAL)
            
    except KeyboardInterrupt:
        print("\nStopping monitor...")

if __name__ == "__main__":
    main()
