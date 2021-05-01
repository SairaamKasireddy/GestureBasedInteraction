import pyautogui


def get_device_information():

    try:
        screen_width, screen_height = pyautogui.size()
        return screen_width, screen_height

    except:
        return 1920, 1080
