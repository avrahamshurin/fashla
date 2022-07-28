from pynput import keyboard
from pynput.keyboard import Key


class KeyboardListener:
    __COMBINATION = {Key.ctrl_l, Key.space}
    __current = set()

    def __init__(self, callback):
        self.__callback = callback

    def __on_press(self, key):
        if key == Key.esc:
            self.__listener.stop()
        if key in self.__COMBINATION:
            self.__current.add(key)
            if all(k in self.__current for k in self.__COMBINATION):
                self.__current.clear()
                self.__callback()

    def __on_release(self, key):
        try:
            self.__current.remove(key)
        except KeyError:
            pass

    def StartListening(self):
        with keyboard.Listener(
            on_press=self.__on_press, on_release=self.__on_release
        ) as self.__listener:
            self.__listener.join()
