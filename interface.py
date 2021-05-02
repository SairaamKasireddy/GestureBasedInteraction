import cv2
import numpy as np


def display_frame(frame, screen_width, screen_height):
    frame_width = int(screen_width / 4)
    frame_height = int(screen_height / 3)
    x_pos = 0
    y_pos = screen_height - frame_height
    frame = cv2.resize(frame, (frame_width, frame_height))
    cv2.moveWindow('frame', x_pos, y_pos)
    cv2.imshow('frame', frame)
    cv2.setWindowProperty('frame', cv2.WND_PROP_TOPMOST, 1)


def display_mask(mask, screen_width, screen_height):
    mask_width = int(screen_width / 4)
    mask_height = int(screen_height / 3)
    x_pos = mask_width
    y_pos = screen_height - mask_height
    mask = cv2.resize(mask, (mask_width, mask_height))
    cv2.moveWindow('mask', x_pos, y_pos)
    cv2.imshow('mask', mask)
    cv2.setWindowProperty('mask', cv2.WND_PROP_TOPMOST, 1)


def show_gesture(gesture_type, screen_width, screen_height):
    window_width = int(screen_width / 4)
    window_height = int(screen_height / 3)
    x_pos = 2 * window_width
    y_pos = screen_height - window_height
    text_x_pos = int(window_width/2)
    text_y_pos = int(window_height/2)
    bg = np.zeros((window_height, window_width, 3), np.uint8)
    bg[:] = (0, 124, 255)
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(bg, str(gesture_type), (text_x_pos-20, text_y_pos), font, 2, (0, 0, 255), 3, cv2.LINE_AA)
    cv2.moveWindow('Gesture', x_pos, y_pos)
    cv2.imshow('Gesture', bg)
    cv2.setWindowProperty('Gesture', cv2.WND_PROP_TOPMOST, 1)
