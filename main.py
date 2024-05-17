import time
from cpu_monitor import CPUMonitor
from memory_monitor import MemoryMonitor
from network_monitor import NetworkMonitor

# ANSI color escape codes
COLOR_RESET = "\033[0m"
COLOR_YELLOW = "\033[93m"  # Yellow for CPU
COLOR_GREEN = "\033[92m"   # Green for Memory
COLOR_BLUE = "\033[94m"    # Blue for Bandwidth

def main():
    cpu_monitor = CPUMonitor()
    memory_monitor = MemoryMonitor()
    network_monitor = NetworkMonitor()

    try:
        while True:
            cpu_output = cpu_monitor.get_cpu_usage()
            memory_output = memory_monitor.get_memory_usage()
            bandwidth_output = network_monitor.get_bandwidth_usage()

            # Apply colors to entire output strings
            cpu_output = f"{COLOR_YELLOW}{cpu_output}{COLOR_RESET}"
            memory_output = f"{COLOR_GREEN}{memory_output}{COLOR_RESET}"
            bandwidth_output = f"{COLOR_BLUE}{bandwidth_output}{COLOR_RESET}"

            print(f"\033[H\033[J{cpu_output} | {memory_output}\n{bandwidth_output}", end='\r')
            time.sleep(0.5)  # Wait for 0.5 seconds before updating again
    except KeyboardInterrupt:
        print("\nExiting...")

if __name__ == "__main__":
    main()
