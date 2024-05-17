import psutil

class CPUMonitor:
    def __init__(self, bars=50):
        self.bars = bars

    def get_cpu_usage(self):
        cpu = psutil.cpu_percent(interval=1)
        return self._format_usage(cpu)

    def _format_usage(self, cpu):
        cpu_percent = cpu / 100.0
        cpu_visual = '#' * int(cpu_percent * self.bars) + '-' * (self.bars - int(cpu_percent * self.bars))
        return f"CPU: [{cpu_visual}] {cpu:.2f}%"
