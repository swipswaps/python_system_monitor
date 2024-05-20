import psutil

class NetworkMonitor:
    def __init__(self):
        self.last_received = psutil.net_io_counters().bytes_recv
        self.last_sent = psutil.net_io_counters().bytes_sent

    def get_bandwidth_usage(self):
        bytes_received = psutil.net_io_counters().bytes_recv
        bytes_sent = psutil.net_io_counters().bytes_sent

        new_received = bytes_received - self.last_received
        new_sent = bytes_sent - self.last_sent

        self.last_received = bytes_received
        self.last_sent = bytes_sent

        received_kb = new_received / 1024
        sent_kb = new_sent / 1024
        total_kb = (new_received + new_sent) / 1024

        return f"Received: {received_kb:.2f} KB | Sent: {sent_kb:.2f} KB | Total: {total_kb:.2f} KB"
