from datetime import timedelta
from sys import argv
from time import time

import psutil as psu

name = argv[0]


def system_info():
    info = {
        "Uptime": timedelta(seconds=time()-psu.boot_time()),
        "CPU in use": f"{psu.cpu_percent(interval=.1)} %",
        "Time on CPU": timedelta(seconds=psu.cpu_times().system+psu.cpu_times().user),
        "Memory in use": f"{psu.virtual_memory().percent} %",
        "Memory available": f"{psu.virtual_memory().available/(1024**3):,.3f} GB",
        "Disc in use": f"{psu.disk_usage('/').percent} %",
        "Disc free": f"{psu.disk_usage('/').free/(1024**3):,.3f} GB",
        "Logical Numbers of CPU": f"{psu.cpu_count()}",
        "Physical Numbers of CPU": f"{psu.cpu_count and psu.cpu_count(logical=False)}",
    }
    print("\n\n     SYSTEM INFO\n\n" + "\n".join([f"{key}: {value:}" for key, value in info.items()]))

system_info()
