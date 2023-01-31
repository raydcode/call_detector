import psutil
from pywinauto import Application


    
def isTeams():
    if "Teams.exe" in (p.name() for p in psutil.process_iter()):
        app = Application(backend='uia').connect(path="Teams.exe")
        window = app.Teams
        call_status = window.child_window(title='Call status').get_value()
        if call_status:
            return True
        else:
            return False
    else:
        for process in psutil.process_iter():
          try:
            if 'chrome.exe' in process.name().lower():
                if 'teams' in process.cmdline()[1]:
                    return True
          except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
        return False
