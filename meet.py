import psutil


def isGoogleMeet():
    for process in psutil.process_iter():
        try:
            if 'chrome.exe' in process.name().lower():
                if 'meet' in process.cmdline()[1]:
                    return True
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False