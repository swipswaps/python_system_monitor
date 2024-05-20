import psutil

class ProcessMonitor:
    def get_running_processes(self, num_processes=10):
        processes = psutil.process_iter(attrs=['name', 'pid', 'username'])
        process_info = []
        for process in processes:
            try:
                name = process.info['name']
                pid = process.info['pid']
                username = process.info['username']
                process_info.append(f"{name} (PID: {pid}, User: {username})")
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                continue
            if len(process_info) >= num_processes:
                break
        return process_info

# Example usage:
if __name__ == "__main__":
    process_monitor = ProcessMonitor()
    processes = process_monitor.get_running_processes()
    for process in processes:
        print(process)
