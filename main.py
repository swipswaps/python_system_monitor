import time
import psutil

# Function to display CPU and memory usage in a visual format
def cpu_and_memory_usage(cpu, memory, bars=50):
    cpu_percent = (cpu / 100.0)
    cpu_visual = '#' * int(cpu_percent * bars) + '-' * (bars - int(cpu_percent * bars))

    memory_percent = (memory / 100.0)
    memory_visual = '#' * int(memory_percent * bars) + '-' * (bars - int(memory_percent * bars))

    return f"CPU: [{cpu_visual}] {cpu:.2f}% | Memory: [{memory_visual}] {memory:.2f}%"

# Function to monitor network bandwidth usage
def bandwidth_monitor(last_received, last_sent):
    # Get the current number of bytes received and sent
    bytes_received = psutil.net_io_counters().bytes_recv
    bytes_sent = psutil.net_io_counters().bytes_sent

    # Calculate the difference from the previous values
    new_received = bytes_received - last_received
    new_sent = bytes_sent - last_sent

    # Convert to kilobytes
    received = new_received / 1024
    sent = new_sent / 1024
    total = (new_received + new_sent) / 1024

    return f"Received: {received:.2f} KB | Sent: {sent:.2f} KB | Total: {total:.2f} KB", bytes_received, bytes_sent

def main():
    # Get the initial values for bytes received and sent
    last_received = psutil.net_io_counters().bytes_recv
    last_sent = psutil.net_io_counters().bytes_sent

    while True:
        # Get CPU, memory, and bandwidth usage
        cpu_memory_output = cpu_and_memory_usage(psutil.cpu_percent(), psutil.virtual_memory().percent)
        bandwidth_output, last_received, last_sent = bandwidth_monitor(last_received, last_sent)

        # Clear the screen and print the updated output
        print(f"\033[H\033[J{cpu_memory_output}\n{bandwidth_output}", end='')
        time.sleep(0.5)  # Wait for 0.5 seconds before updating again

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nExiting...")