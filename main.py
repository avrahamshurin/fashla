from keyboard_listener import KeyboardListener
from keyboard_layout_handler import KeyboardLayoutHandler
import clipboard_handler
import keyboard_operations


def Translate():
    original_in_clipboard = clipboard_handler.GetSavedInClipboard()

    text_to_translate = GetSelectedText()

    klh = KeyboardLayoutHandler()
    original_layout_id = klh.GetCurrentKeyboardLayout()
    keyboard_operations.ChangeKeyboardLanguage()
    new_layout_id = klh.GetCurrentKeyboardLayout()
    translated = klh.KeyboardLayoutTranslator(
        text_to_translate, original_layout_id, new_layout_id
    )
    SendToSelectedText(translated)

    clipboard_handler.SaveToClipboard(original_in_clipboard)


def GetSelectedText():
    keyboard_operations.CopySelectedTextToClipboard()
    return clipboard_handler.GetSavedInClipboard()


def SendToSelectedText(to_send):
    clipboard_handler.SaveToClipboard(to_send)
    keyboard_operations.PasteText()


def main():
    listener = KeyboardListener(Translate)
    listener.StartListening()


if __name__ == "__main__":
    main()
