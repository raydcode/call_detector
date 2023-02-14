

from pywinauto import Application

app = Application(backend="uia").connect(title_re=".*Teams.*")

# Get the main window
main_window = app.window(title_re=".*Teams.*")

# Check if the call button is enabled
call_button = main_window.child_window(title="Call", control_type="Button")
if call_button.is_enabled():
    print("No active call")
else:
    print("There is an active call")

    
# def isTeams():
#     # if "Teams.exe" in (p.name() for p in psutil.process_iter()):
#     #     app = Application(backend='uia').connect(path="Teams.exe")
#     #     window = app.Teams
#     #     call_status = window.child_window(title='Call status').get_value()
#     #     if call_status:
#     #         return True
#     #     else:
#     #         return False
#     # else:
#     #     for process in psutil.process_iter():
#     #       try:
#     #         if 'chrome.exe' in process.name().lower():
#     #             if 'teams' in process.cmdline()[1]:
#     #                 return True
#     #       except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
#     #         pass
#     #     return False
