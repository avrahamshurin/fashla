import ctypes
import win32api

class KeyboardLayoutHandler:

    def GetCurrentKeyboardLayout(self):
        user32 = ctypes.WinDLL("user32", use_last_error=True)
        handle = user32.GetForegroundWindow()
        threadid = user32.GetWindowThreadProcessId(handle, 0)
        layout_id = user32.GetKeyboardLayout(threadid)
        language_id = layout_id & (2**16 - 1)

        return language_id

    def KeyboardLayoutTranslator(self, text_to_translate, from_layout, to_layout):
            keys = [self.__CharToVk(c, from_layout) for c in text_to_translate]
            translated = "".join([self.__VkToChar(key, to_layout) for key in keys])
            return translated

    def __CharToVk(self, char, layout):
        return win32api.VkKeyScanEx(char, layout)
    
    def __VkToChar(self, vk, layout):
        _ToUnicodeEx = ctypes.WinDLL("user32").ToUnicodeEx
        _ToUnicodeEx.argtypes = [
            ctypes.c_uint,
            ctypes.c_uint,
            ctypes.POINTER(ctypes.c_char),
            ctypes.POINTER(ctypes.c_wchar),
            ctypes.c_int,
            ctypes.c_uint,
            ctypes.c_void_p,
        ]
        _ToUnicodeEx.restype = ctypes.c_int

        kst = ctypes.create_string_buffer(256)
        if vk >> 8 == 1:
            kst[16] = 0x80
        b = ctypes.create_unicode_buffer(5)
        _ToUnicodeEx(vk, 0, kst, b, 5, 0, layout)
        return b.value
