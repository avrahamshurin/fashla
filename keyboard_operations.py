import pyautogui as pya
import time


def SendKeys(*key_strings):
    pya.hotkey(*key_strings)


def ChangeKeyboardLanguage():
    SendKeys("alt", "shift")
    time.sleep(0.5)


def CopySelectedTextToClipboard():
    SendKeys("ctrl", "c")


def PasteText():
    SendKeys("ctrl", "v")
