import time
from cpu_monitor import CPUMonitor
from memory_monitor import MemoryMonitor
from network_monitor import NetworkMonitor
from system_info import SystemInfo
from processes import ProcessMonitor

# ANSI color escape codes
COLOR_RESET = "\033[0m"
COLOR_YELLOW = "\033[93m"  # Yellow for CPU
COLOR_GREEN = "\033[92m"   # Green for Memory
COLOR_BLUE = "\033[94m"    # Blue for Bandwidth
COLOR_CYAN = "\033[96m"    # Cyan for Headers

def main():
    cpu_monitor = CPUMonitor()
    memory_monitor = MemoryMonitor()
    network_monitor = NetworkMonitor()
    system_info = SystemInfo()
    process_monitor = ProcessMonitor()

    try:
        while True:
            # Get real-time data
            cpu_output = cpu_monitor.get_cpu_usage()
            memory_output = memory_monitor.get_memory_usage()
            bandwidth_output = network_monitor.get_bandwidth_usage()
            sys_info_output = system_info.get_system_info()
            processes_output = process_monitor.get_running_processes(num_processes=10)

            # Apply colors to entire output strings
            cpu_output = f"{COLOR_YELLOW}{cpu_output}{COLOR_RESET}"
            memory_output = f"{COLOR_GREEN}{memory_output}{COLOR_RESET}"
            bandwidth_output = f"{COLOR_BLUE}{bandwidth_output.replace('Received', '↓').replace('Sent', '↑')}{COLOR_RESET}"
            sys_info_output = f"{COLOR_CYAN}{sys_info_output}{COLOR_RESET}"
            processes_output = "\n".join([f"{COLOR_CYAN}Running Processes{COLOR_RESET}", "-----------------"] + processes_output)

            # Clear screen
            print("\033c", end='')

            # Print headers
            print(f"{COLOR_CYAN}CPU & Memory      Network{COLOR_RESET}")
            print(f"{COLOR_CYAN}-------------      -------{COLOR_RESET}")

            # Print meters and system info
            print(f"{cpu_output}      {bandwidth_output}")
            print(f"{memory_output}")
            print(f"{COLOR_CYAN}System Info{COLOR_RESET}")
            print(f"{COLOR_CYAN}-----------{COLOR_RESET}")
            sys_info_lines = [line[:40] for line in sys_info_output.split("\n")]
            for line in sys_info_lines:
                print(line)

            # Print Running Processes
            print(processes_output)

            # Move cursor to the top
            print("\033[6A", end='')

            time.sleep(0.5)  # Wait for 0.5 seconds before updating again

    except KeyboardInterrupt:
        print("\nExiting...")

if __name__ == "__main__":
    main()