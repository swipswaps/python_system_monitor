
---

# Python System Monitor

A terminal-based system monitor application built with Python and the `curses` library. This application provides real-time monitoring of CPU usage, memory usage, network bandwidth, system information, and running processes.

## Features

- **CPU Usage**: Displays overall CPU usage as well as usage per core.
- **Memory Usage**: Displays current memory and swap usage.
- **Network Usage**: Shows network bandwidth usage.
- **System Information**: Provides details about the operating system, Python version, hostname, IP address, CPU cores, RAM, and system uptime.
- **Running Processes**: Lists top running processes by memory usage with the ability to highlight and kill processes using the keyboard and mouse.

## Prerequisites

- Python 3.6 or higher
- `psutil` library

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/Hillary520/python_system_monitor.git
    cd python_system_monitor
    ```

2. Install the required Python libraries:
    ```sh
    pip install psutil
    ```

## Usage

Run the main script to start the system monitor:
```sh
python3 main.py
```

## Modules

- `cpu_monitor.py`: Contains the `CPUMonitor` class to get CPU usage information.
- `memory_monitor.py`: Contains the `MemoryMonitor` class to get memory and swap usage.
- `network_monitor.py`: Contains the `NetworkMonitor` class to get network bandwidth usage.
- `system_info.py`: Contains the `SystemInfo` class to get system information.
- `processes.py`: Contains the `ProcessMonitor` class to get a list of running processes.

## Controls

- **Arrow Keys**: Navigate through the list of processes.
- **Mouse Click**: Click to select/highlight a process.
- **K**: Kill the highlighted process.

