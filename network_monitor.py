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

        received = new_received / 1024
        sent = new_sent / 1024
        total = (new_received + new_sent) / 1024

        return f"Received: {received:.2f} KB | Sent: {sent:.2f} KB | Total: {total:.2f} KB"
