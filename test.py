import psutil
import pymem

# Define the keywords to search for in the browser's memory
keywords = ['video', 'audio', 'call']

# Get a list of all running processes
processes = psutil.process_iter()

# Loop through all the processes and check which ones are associated with web browsers
for process in processes:
    try:
        process_name = process.name().lower()
        if 'chrome' in process_name or 'firefox' in process_name:
            pm = pymem.Pymem()
            pm.open_process(process.pid)
            for keyword in keywords:
                if keyword.encode() in pm.read_bytes(pm.base_address, pm.get_size()):
                    print(f"Browser with PID {process.pid} has an active call.")
                    break
            pm.close_process()
    except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
        pass
