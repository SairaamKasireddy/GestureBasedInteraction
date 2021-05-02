import pyautogui


def mouse_click(x, y):
    pyautogui.click(x=x, y=y)


def move_mouse(x, y):
    pyautogui.moveTo(x, y)


def shift_tab():
    pyautogui.keyDown('shift')
    pyautogui.press('tab')
    pyautogui.keyUp('shift')


def spacebar():
    pyautogui.press('space')


def tab():
    pyautogui.press('tab')


def volume_down():
    pyautogui.press('volumedown')


def volume_up():
    pyautogui.press('volumeup')
