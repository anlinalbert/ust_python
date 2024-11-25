import win32gui
import win32con


def set_wallpaper(image):
    """Function to set wallpaper."""
    win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER, image, win32con.SPIF_UPDATEINIFILE | win32con.SPIF_SENDCHANGE)


set_wallpaper(r"C:\Users\Administrator\Desktop\UST Training\Practice_Programs\day20\f957c2258464e96fac690a3b347ca02e.png")
