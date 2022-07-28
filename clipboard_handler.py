import pyperclip


def GetSavedInClipboard():
    return pyperclip.paste()


def SaveToClipboard(value):
    pyperclip.copy(value)
