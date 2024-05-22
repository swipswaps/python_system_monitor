import psutil

class CPUMonitor:
    def __init__(self, bars=50):
        self.bars = bars

    def get_cpu_usage(self):
        cpu = psutil.cpu_percent(interval=1)
        return self._format_usage(cpu)

    def get_cpu_cores_usage(self):
        cores = psutil.cpu_percent(interval=1, percpu=True)
        return [self._format_core_usage(idx, core) for idx, core in enumerate(cores)]

    def _format_usage(self, cpu):
        cpu_percent = cpu / 100.0
        cpu_visual = '#' * int(cpu_percent * self.bars) + '-' * (self.bars - int(cpu_percent * self.bars))
        return f"CPU: [{cpu_visual}] {cpu:.2f}%"

    def _format_core_usage(self, core_idx, core):
        core_percent = core / 100.0
        core_visual = '#' * int(core_percent * self.bars) + '-' * (self.bars - int(core_percent * self.bars))
        return f"Core {core_idx}: [{core_visual}] {core:.2f}%"