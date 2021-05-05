import cv2
import time
import pyautogui


def mouse_click(x, y):
    pyautogui.click(x=x, y=y)


def move_mouse(contour, screen_width, screen_height, frame_width, frame_height):
    M = cv2.moments(contour)
    extTop1 = tuple(contour[contour[:, :, 1].argmin()][0])
    # cX = int(M["m10"] / M["m00"])
    # cY = int(M["m01"] / M["m00"])
    cX = int(extTop1[0]*screen_width/frame_width)
    cY = int(extTop1[1] *screen_height/frame_height)
    pyautogui.moveTo(cX, cY)


def shift_tab():
    pyautogui.keyDown('shift')
    pyautogui.press('tab')
    pyautogui.keyUp('shift')


def type_number(num):
    pyautogui.write(num, interval=0.25)


def spacebar():
    pyautogui.press('space')


def tab():
    pyautogui.press('tab')


def volume_down():
    pyautogui.press('volumedown')


def volume_up():
    pyautogui.press('volumeup')


def perform_action(action_type, prev_timestamp):
    if (time.time() - prev_timestamp) < 2.0:
        return prev_timestamp
    if action_type == "":
        print('nothing happened')
    action = int(action_type)
    if action == 0:
        volume_down()
    elif action == 1:
        pass
    elif action == 2:
        spacebar()
    elif action == 3:
        volume_up()
    elif action == 4:
        shift_tab()
    elif action == 5:
        tab()
    elif action == 6:
        tab()
    else:
        pass
    return time.time()
