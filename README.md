# System Monitor

This Python script is a simple system monitor that displays CPU, memory, and network bandwidth usage in a terminal. It uses the `psutil` library to retrieve system information.

## Features

- Displays CPU and memory usage in a visual format using hash (`#`) and hyphen (`-`) characters.
- Monitors network bandwidth usage and shows the received, sent, and total data transfer rates.
- Continuously updates the output every 0.5 seconds.
- Clears the terminal screen before displaying the updated output.

## Requirements

- Python 3.x
- `psutil` library (install with `pip install psutil`)

## Usage

1. Clone or download the repository.
2. Open a terminal and navigate to the project directory.
3. Run the script with `python system_monitor.py`.
4. The output will be displayed in the terminal, updating every 0.5 seconds.
5. Press `Ctrl+C` to exit the program.

## Todo

The following features can be added to enhance the system monitor:

### System Information

Add functionality to display additional system information such as:

- Operating system name and version
- System uptime
- CPU model and number of cores
- Total and available RAM

### Running Processes

Implement a feature to display a list of currently running processes on the system, including:

- Process name
- Process ID (PID)
- CPU and memory usage for each process

You can use the `psutil.process_iter()` function to iterate over all running processes and retrieve the necessary information.

## Contributing

Contributions are welcome! If you find any issues or have ideas for improvements, please open an issue or submit a pull request.

