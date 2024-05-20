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
            memory_output = memory_monitor.get_memory_usage()
            bandwidth_output = network_monitor.get_bandwidth_usage()
            sys_info_output = system_info.get_system_info()
            processes_output = process_monitor.get_running_processes(num_processes=10)

            # Clear screen
            stdscr.clear()

            # Define color pairs
            curses.start_color()
            curses.init_pair(1, curses.COLOR_YELLOW, curses.COLOR_BLACK)
            curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
            curses.init_pair(3, curses.COLOR_BLUE, curses.COLOR_BLACK)
            curses.init_pair(4, curses.COLOR_CYAN, curses.COLOR_BLACK)
            curses.init_pair(5, curses.COLOR_RED, curses.COLOR_BLACK)

            # Print CPU and Memory Usage
            stdscr.addstr(0, 0, "CPU Usage", curses.color_pair(4))
            stdscr.addstr(1, 0, cpu_output[:half_width], curses.color_pair(1))
            stdscr.addstr(2, 0, "Memory Usage", curses.color_pair(4))
            stdscr.addstr(3, 0, memory_output[:half_width], curses.color_pair(2))

            # Print Bandwidth Usage
            stdscr.addstr(0, half_width, "Network Usage", curses.color_pair(4))
            stdscr.addstr(1, half_width, bandwidth_output.replace('Received', '↓').replace('Sent', '↑')[:half_width], curses.color_pair(3))

            # Print System Info
            stdscr.addstr(5, 0, "System Info", curses.color_pair(4))
            stdscr.addstr(6, 0, "-----------", curses.color_pair(4))
            sys_info_lines = [line[:half_width] for line in sys_info_output.split("\n")]
            for idx, line in enumerate(sys_info_lines):
                if 7 + idx < height:
                    stdscr.addstr(7 + idx, 0, line, curses.color_pair(4))

            # Print Running Processes
            stdscr.addstr(5, half_width, "Running Processes", curses.color_pair(4))
            stdscr.addstr(6, half_width, "-----------------", curses.color_pair(4))
            for idx, process in enumerate(processes_output):
                if 7 + idx < height:
                    stdscr.addstr(7 + idx, half_width, process[:half_width], curses.color_pair(5))

            stdscr.refresh()
            time.sleep(0.5)  # Wait for 0.5 seconds before updating again

    except KeyboardInterrupt:
        print("\nExiting...")

if __name__ == "__main__":
    curses.wrapper(main)
