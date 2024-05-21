import curses
import time
from cpu_monitor import CPUMonitor
from memory_monitor import MemoryMonitor
from network_monitor import NetworkMonitor
from system_info import SystemInfo
from processes import ProcessMonitor

def main(stdscr):
    # Clear screen
    stdscr.clear()
    curses.curs_set(0)  # Hide the cursor

    cpu_monitor = CPUMonitor()
    memory_monitor = MemoryMonitor()
    network_monitor = NetworkMonitor()
    system_info = SystemInfo()
    process_monitor = ProcessMonitor()

    try:
        while True:
            # Get screen dimensions
            height, width = stdscr.getmaxyx()
            half_width = width // 2

            # Get real-time data
            cpu_output = cpu_monitor.get_cpu_usage()
            cpu_cores_output = cpu_monitor.get_cpu_cores_usage()
            memory_output = memory_monitor.get_memory_usage()
            swap_output = memory_monitor.get_swap_usage()
            bandwidth_output = network_monitor.get_bandwidth_usage()
            sys_info_output = system_info.get_system_info()
            processes_output = process_monitor.get_running_processes(num_processes=10)

            # Clear screen
            stdscr.clear()

            # Define color pairs
            curses.start_color()
            curses.init_pair(1, curses.COLOR_GREEN, curses.COLOR_BLACK)  # CPU color
            curses.init_pair(2, curses.COLOR_YELLOW, curses.COLOR_BLACK) # CPU Cores color
            curses.init_pair(3, curses.COLOR_BLUE, curses.COLOR_BLACK)   # Network color
            curses.init_pair(4, curses.COLOR_CYAN, curses.COLOR_BLACK)   # Headers color
            curses.init_pair(5, curses.COLOR_RED, curses.COLOR_BLACK)    # Processes color
            curses.init_pair(6, curses.COLOR_WHITE, curses.COLOR_BLACK)  # General text color

            # Print CPU Usage
            stdscr.addstr(0, 0, "CPU Usage", curses.color_pair(4) | curses.A_BOLD)
            stdscr.addstr(1, 0, cpu_output[:half_width], curses.color_pair(1))
            for idx, core_output in enumerate(cpu_cores_output[:len(cpu_cores_output) // 2]):
                if 2 + idx < height:
                    stdscr.addstr(2 + idx, 0, core_output[:half_width], curses.color_pair(2))

            # Print Memory Usage and Network Usage
            mem_net_start = 3 + len(cpu_cores_output) // 2
            stdscr.addstr(mem_net_start, 0, "Memory Usage", curses.color_pair(4) | curses.A_BOLD)
            stdscr.addstr(mem_net_start + 1, 0, memory_output[:half_width], curses.color_pair(6))
            stdscr.addstr(mem_net_start + 2, 0, swap_output[:half_width], curses.color_pair(6))
            stdscr.addstr(mem_net_start + 4, 0, "Network Usage", curses.color_pair(4) | curses.A_BOLD)
            stdscr.addstr(mem_net_start + 5, 0, bandwidth_output.replace('Received', '↓').replace('Sent', '↑')[:half_width], curses.color_pair(3))

            # Print CPU Cores in the second column
            stdscr.addstr(0, half_width, "CPU Cores", curses.color_pair(4) | curses.A_BOLD)
            for idx, core_output in enumerate(cpu_cores_output[len(cpu_cores_output) // 2:]):
                if 1 + idx < height:
                    stdscr.addstr(1 + idx, half_width, core_output[:half_width], curses.color_pair(2))

            # Print System Info
            sys_info_start = mem_net_start + 7
            stdscr.addstr(sys_info_start, 0, "System Info", curses.color_pair(4) | curses.A_BOLD)
            sys_info_lines = [line[:half_width] for line in sys_info_output.split("\n")]
            for idx, line in enumerate(sys_info_lines):
                if sys_info_start + 1 + idx < height:
                    stdscr.addstr(sys_info_start + 1 + idx, 0, line, curses.color_pair(6))

            # Print Running Processes in a table format
            process_start = sys_info_start
            stdscr.addstr(process_start, half_width, "Running Processes", curses.color_pair(4) | curses.A_BOLD)
            stdscr.addstr(process_start + 1, half_width, f"{'PID':<8} {'USER':<12} {'NAME':<25} {'MEM%':<8}", curses.color_pair(6) | curses.A_BOLD)
            processes_output = sorted(processes_output, key=lambda p: p['memory_percent'], reverse=True)
            for idx, process in enumerate(processes_output):
                process_info = f"{process['pid']:<8} {process['username']:<12} {process['name']:<25} {process['memory_percent']:<8.2f}"
                if process_start + 2 + idx < height:
                    stdscr.addstr(process_start + 2 + idx, half_width, process_info[:half_width], curses.color_pair(5))

            stdscr.refresh()
            time.sleep(0.5)  # Wait for 0.5 seconds before updating again

    except KeyboardInterrupt:
        print("\nExiting...")

if __name__ == "__main__":
    curses.wrapper(main)
