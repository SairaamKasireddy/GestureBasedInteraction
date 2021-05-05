import cv2
import interface
import numpy as np


def get_area_of_interest(frame):

    frame_width, frame_height = frame.shape[1], frame.shape[0]

    area_of_interest = frame[100:frame_height, 100:frame_width]

    return area_of_interest, 100, 100, frame_width, frame_height


def get_contour(area_of_interest, lower_skin_bound, upper_skin_bound, screen_width, screen_height):
    area_of_interest_hsv = cv2.cvtColor(area_of_interest, cv2.COLOR_BGR2HSV)

    masked_input = cv2.inRange(area_of_interest_hsv, lower_skin_bound, upper_skin_bound)

    kernel = np.ones((3, 3), np.uint8)
    masked_input = cv2.dilate(masked_input, kernel, iterations=4)
    masked_input = cv2.GaussianBlur(masked_input, (5, 5), 100)

    interface.display_mask(masked_input, screen_width, screen_height)

    contours, hierarchy = cv2.findContours(masked_input, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    contour = max(contours, key=lambda x: cv2.contourArea(x))
    return contour


