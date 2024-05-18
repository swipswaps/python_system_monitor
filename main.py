import time
from cpu_monitor import CPUMonitor
from memory_monitor import MemoryMonitor
from network_monitor import NetworkMonitor
from system_info import SystemInfo

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

    try:
        while True:
            # Get real-time data
            cpu_output = cpu_monitor.get_cpu_usage()
            memory_output = memory_monitor.get_memory_usage()
            bandwidth_output = network_monitor.get_bandwidth_usage()
            sys_info_output = system_info.get_system_info()

            # Apply colors to entire output strings
            cpu_output = f"{COLOR_YELLOW}{cpu_output}{COLOR_RESET}"
            memory_output = f"{COLOR_GREEN}{memory_output}{COLOR_RESET}"
            bandwidth_output = f"{COLOR_BLUE}{bandwidth_output}{COLOR_RESET}"
            sys_info_output = f"{COLOR_CYAN}{sys_info_output}{COLOR_RESET}"

            # Clear screen
            print("\033c", end='')

            # Print headers
            print(f"{COLOR_CYAN}CPU & Memory{COLOR_RESET}")
            print(f"{COLOR_CYAN}------------{COLOR_RESET}")

            # Print CPU and Memory meters
            print(f"{cpu_output}\n{memory_output}\n")

            # Print Network header
            print(f"{COLOR_CYAN}Network{COLOR_RESET}")
            print(f"{COLOR_CYAN}-------{COLOR_RESET}")

            # Print Network meter
            print(f"{bandwidth_output}\n")

            # Print System Info header
            print(f"{COLOR_CYAN}System Info{COLOR_RESET}")
            print(f"{COLOR_CYAN}-----------{COLOR_RESET}")

            # Print System Info
            print(sys_info_output)

            # Move cursor to the top
            print("\033[10A", end='')

            time.sleep(0.5)  # Wait for 0.5 seconds before updating again

    except KeyboardInterrupt:
        print("\nExiting...")

if __name__ == "__main__":
    main()