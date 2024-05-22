import psutil

class MemoryMonitor:
    def __init__(self, bars=50):
        self.bars = bars

    def get_memory_usage(self):
        memory = psutil.virtual_memory().percent
        return self._format_usage(memory)

    def _format_usage(self, memory):
        memory_percent = memory / 100.0
        memory_visual = '#' * int(memory_percent * self.bars) + '-' * (self.bars - int(memory_percent * self.bars))
        return f"Memory: [{memory_visual}] {memory:.2f}%"

    def get_swap_usage(self):
        swap = psutil.swap_memory().percent
        return self._format_usage_swap(swap)

    def _format_usage_swap(self, swap):
        swap_percent = swap / 100.0
        swap_visual = '#' * int(swap_percent * self.bars) + '-' * (self.bars - int(swap_percent * self.bars))
        return f"Swap: [{swap_visual}] {swap:.2f}%"