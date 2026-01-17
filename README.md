# PowerLog (C++)

A C++ utility that bridges **Electrical Engineering** and **Computer Science**. It simulates an IoT sensor monitoring a server room's power supply (Voltage/Current), logging data to a CSV file for analysis.

## Project Concept
This tool connects physical infrastructure monitoring with software automation. It:
1.  **Simulates** a hardware sensor reading Voltage (V) and Current (I).
2.  **Calculates** Power consumption (P = V * I) in real-time.
3.  **Detects** electrical faults (Surges > 240V, Brownouts < 215V).
4.  **Logs** all incidents to `power_log.csv` for historical analysis.

## Compilation

### Using MinGW (g++)
```powershell
g++ PowerLog.cpp -o PowerLog.exe
```

## Usage
1.  Run the tool:
    ```powershell
    ./PowerLog.exe
    ```
2.  Observe the real-time console feed. Faults will be highlighted in **RED**.
3.  Check the generated `power_log.csv` file to see the persistent data.

This project demonstrates skills in **C++ I/O Streams**, **Data Logging**, and **simulation logic**.
