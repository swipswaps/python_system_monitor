import psutil

class ProcessMonitor:
    def get_running_processes(self, num_processes=10):
        processes = []
        for process in psutil.process_iter(attrs=['pid', 'name', 'username', 'memory_percent']):
            try:
                processes.append(process.info)
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                continue
        sorted_processes = sorted(processes, key=lambda p: p['memory_percent'], reverse=True)
        return sorted_processes[:num_processes]