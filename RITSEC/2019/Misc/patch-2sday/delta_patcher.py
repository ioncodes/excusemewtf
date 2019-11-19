import ctypes
import ctypes.wintypes

LPBUFFER = ctypes.POINTER(ctypes.c_char)

DELTA_FLAG_TYPE = ctypes.c_ulonglong

class DELTA_INPUT(ctypes.Structure):
    _fields_ = [
        ("lpStart", LPBUFFER),
        ("uSize", ctypes.wintypes.ULONG),
        ("Editable", ctypes.wintypes.BOOL)]

class DELTA_OUTPUT(ctypes.Structure):
    _fields_ = [
        ("lpStart", LPBUFFER),
        ("uSize", ctypes.wintypes.ULONG)]

DELTA_FLAG_NONE = 0
DELTA_APPLY_FLAG_ALLOW_PA19 = 1

def _winerror_on_failure(result, func, arguments):
    if not result:
        raise ctypes.WinError()
    return result

_dll = ctypes.windll.msdelta

_applyDeltaB = _dll.ApplyDeltaB
_applyDeltaB.argtypes = [DELTA_FLAG_TYPE, DELTA_INPUT, DELTA_INPUT, ctypes.POINTER(DELTA_OUTPUT)]
_applyDeltaB.errcheck = _winerror_on_failure

_applyDeltaW = _dll.ApplyDeltaW
_applyDeltaW.argtypes = [DELTA_FLAG_TYPE, ctypes.wintypes.LPCWSTR, ctypes.wintypes.LPCWSTR, ctypes.wintypes.LPCWSTR]
_applyDeltaW.errcheck = _winerror_on_failure

_deltaFree = _dll.DeltaFree
_deltaFree.argtypes = [LPBUFFER]
_deltaFree.errcheck = _winerror_on_failure

def ApplyDeltaB(source, delta, flags = DELTA_APPLY_FLAG_ALLOW_PA19):
    diSource = DELTA_INPUT(ctypes.create_string_buffer(source), len(source), False)
    diDelta = DELTA_INPUT(ctypes.create_string_buffer(delta), len(delta), False)    
    doResult = DELTA_OUTPUT()

    _applyDeltaB(flags, diSource, diDelta, ctypes.byref(doResult))

    result = doResult.lpStart[:doResult.uSize]
    _deltaFree(doResult.lpStart)

    return result

def ApplyDelta(sourcePath, deltaPath, targetPath, flags = DELTA_APPLY_FLAG_ALLOW_PA19):
    _applyDeltaW(flags, sourcePath, deltaPath, targetPath)

with open("patch-tuesday1", "rb") as file:
    delta = file.read()[4:]
with open("win32k.patched.sys", "rb") as file:
    source = file.read()

patched = ApplyDeltaB(source, delta)
with open("win32k.actually.patched.sys", "wb") as file:
    file.write(patched)