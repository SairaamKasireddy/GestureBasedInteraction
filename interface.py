import cv2


def display_frame(frame, screen_width, screen_height):
    frame_width = int(screen_width / 4)
    frame_height = int(screen_height / 3)
    x_pos = screen_width - frame_width
    y_pos = screen_height - frame_height
    frame = cv2.resize(frame, (frame_width, frame_height))
    cv2.moveWindow('frame', x_pos, y_pos)
    cv2.imshow('frame', frame)
    cv2.setWindowProperty('frame', cv2.WND_PROP_TOPMOST, 1)


def display_mask(mask, screen_width, screen_height):
    mask_width = int(screen_width / 4)
    mask_height = int(screen_height / 3)
    x_pos = screen_width - 2 * mask_width
    y_pos = screen_height - mask_height
    mask = cv2.resize(mask, (mask_width, mask_height))
    cv2.moveWindow('mask', x_pos, y_pos)
    cv2.imshow('mask', mask)
    cv2.setWindowProperty('mask', cv2.WND_PROP_TOPMOST, 1)
