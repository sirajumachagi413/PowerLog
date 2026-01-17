# PowerLog (Python)

A Python utility that bridges **Electrical Engineering** and **Computer Science**. It simulates an IoT sensor monitoring a server room's power supply (Voltage/Current), logging data to a CSV file for analysis.

## Project Concept
This tool connects physical infrastructure monitoring with software automation. It:
1.  **Simulates** a hardware sensor reading Voltage (V) and Current (I).
2.  **Calculates** Power consumption (P = V * I) in real-time.
3.  **Detects** electrical faults (Surges > 245V, Brownouts < 210V).
4.  **Logs** all incidents to `power_data_py.csv` for historical analysis.

## Requirements
- Python 3.x

## Usage
1.  Run the tool:
    ```powershell
    python power_log.py
    ```
2.  Observe the real-time console feed. Faults will be highlighted in **RED**.
3.  Check the generated `power_data_py.csv` file to see the persistent data.

This project demonstrates skills in **Python**, **CSV File Handling**, **Real-time Simulation**, and **Data Logging**.
