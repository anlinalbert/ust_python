import win32api
import win32gui

print(f"Windows metrics: {win32api.GetVersion()}\nComputer name: {win32api.GetComputerName()}\nComputer metric: "
      f"{win32api.GetSystemMetrics(0)}")

# Message box
win32gui.MessageBox(0, "Hello Pywin32", "Message box demo", 1)
win32gui.MessageBox(0, "Hello Pywin32", "Message box demo", 5)
