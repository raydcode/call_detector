import psutil




def isSkype():
    if "skype.exe" in (p.name() for p in psutil.process_iter()):
        skype = Skype4Py.Skype()
        skype.Attach()
        if skype.Client.IsRunning:
            call = skype.ActiveCalls()
            if call:
                return True
            else:
                return False
        else:
            return False
    else:
        for process in psutil.process_iter():
         try:
            if 'chrome.exe' in process.name().lower():
                if 'skype' in process.cmdline()[1]:
                    return True
         except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
        return False
    
    
# def isSkype():
#   for process in psutil.process_iter():
#     try:
#         if 'skype.exe' in process.name().lower():
#             return True
#     except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
#         pass
#   return False
