import platform
import psutil
import time
import socket
import subprocess

class SystemInfo:
    def get_system_info(self):
        os_name = platform.system()
        os_version = platform.version()
        python_version = platform.python_version()
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
        cpu_model = platform.processor()
        cpu_cores = psutil.cpu_count(logical=True)
        total_ram = psutil.virtual_memory().total / (1024 ** 3)  # Convert to GB
        available_ram = psutil.virtual_memory().available / (1024 ** 3)  # Convert to GB
        uptime = time.time() - psutil.boot_time()
        uptime_str = self._format_uptime(uptime)
        disk_usage = self._get_disk_usage()
        network_interfaces = self._get_network_interfaces()
        battery_status = self._get_battery_status()
        battery_health = self._get_battery_health()

        sys_info_output = (
            f"OS: {os_name}\n"
            f"Python: {python_version}\n"
            f"Hostname: {hostname}\n"
            f"IP Address: {ip_address}\n"
            f"CPU: {cpu_model} ({cpu_cores} cores)\n"
            f"RAM: {total_ram:.2f} GB total, {available_ram:.2f} GB available\n"
            f"Uptime: {uptime_str}\n"
            f"Disk Usage: {disk_usage}\n"
            f"Network Interfaces: {network_interfaces}\n"
            f"Battery: {battery_status}\n"
            f"Battery Health: {battery_health}"
        )

        return sys_info_output

    def _format_uptime(self, seconds):
        mins, secs = divmod(seconds, 60)
        hours, mins = divmod(mins, 60)
        days, hours = divmod(hours, 24)
        return f"{int(days)}d {int(hours)}h {int(mins)}m {int(secs)}s"

    def _get_disk_usage(self):
        disk_usage = psutil.disk_usage('/')
        total = disk_usage.total / (1024 ** 3)  # Convert to GB
        used = disk_usage.used / (1024 ** 3)  # Convert to GB
        free = disk_usage.free / (1024 ** 3)  # Convert to GB
        return f"{used:.2f} GB used / {total:.2f} GB total / {free:.2f} GB free"

    def _get_network_interfaces(self):
        interfaces = psutil.net_if_addrs()
        interface_details = []
        for interface, addrs in interfaces.items():
            for addr in addrs:
                if addr.family == socket.AF_INET:
                    interface_details.append(f"{interface}: {addr.address}")
        return ', '.join(interface_details)

    def _get_battery_status(self):
        battery = psutil.sensors_battery()
        if battery:
            percent = battery.percent
            plugged = "plugged in" if battery.power_plugged else "not plugged in"
            secs_left = battery.secsleft
            if secs_left == psutil.POWER_TIME_UNLIMITED:
                time_left = "charging"
            elif secs_left == psutil.POWER_TIME_UNKNOWN:
                time_left = "unknown"
            else:
                time_left = self._format_uptime(secs_left)
            return f"{percent}% ({plugged}, {time_left} remaining)"
        else:
            return "No battery detected"

    def _get_battery_health(self):
        os_name = platform.system()
        try:
            if os_name == 'Darwin':  # macOS
                health_info = subprocess.check_output(
                    ["ioreg", "-r", "-c", "AppleSmartBattery", "-k", "DesignCapacity", "-k", "MaxCapacity"],
                    universal_newlines=True
                )
                design_capacity = int(self._parse_health_info(health_info, 'DesignCapacity'))
                max_capacity = int(self._parse_health_info(health_info, 'MaxCapacity'))
                health_percent = (max_capacity / design_capacity) * 100
                return f"{health_percent:.2f}%"
            elif os_name == 'Windows':  # Windows
                health_info = subprocess.check_output(
                    ["powercfg", "/batteryreport", "/output", "battery_report.html"],
                    universal_newlines=True
                )
                # Read and parse the battery_report.html to get battery health information
                with open("battery_report.html", "r") as file:
                    report = file.read()
                design_capacity = int(self._parse_battery_report(report, 'DESIGN CAPACITY'))
                full_charge_capacity = int(self._parse_battery_report(report, 'FULL CHARGE CAPACITY'))
                health_percent = (full_charge_capacity / design_capacity) * 100
                return f"{health_percent:.2f}%"
            elif os_name == 'Linux':  # Linux
                with open('/sys/class/power_supply/BAT0/charge_full', 'r') as file:
                    full_charge_capacity = int(file.read().strip())
                with open('/sys/class/power_supply/BAT0/charge_full_design', 'r') as file:
                    design_capacity = int(file.read().strip())
                health_percent = (full_charge_capacity / design_capacity) * 100
                return f"{health_percent:.2f}%"
            else:
                return "Unsupported OS"
        except Exception as e:
            return f"Error retrieving battery health: {e}"

    def _parse_health_info(self, health_info, key):
        return health_info.split(f"{key} = ")[1].split('\n')[0].strip()

    def _parse_battery_report(self, report, key):
        return report.split(f'{key}')[1].split('<td>')[1].split(' mWh')[0].replace(',', '')