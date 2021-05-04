import cv2
import math
import numpy as np


def get_defects(contour):

    epsilon = 0.0005 * cv2.arcLength(contour, True)
    approx = cv2.approxPolyDP(contour, epsilon, True)

    hull = cv2.convexHull(contour)
    hull_area = cv2.contourArea(hull)
    contour_area = cv2.contourArea(contour)

    area_ratio = ((hull_area - contour_area) / contour_area) * 100
    hull = cv2.convexHull(approx, returnPoints=False)
    defects = cv2.convexityDefects(approx, hull)

    return defects, contour_area, area_ratio, approx


def count_defects(defects, approx, area_of_interest):

    number_of_defects = 0

    for i in range(defects.shape[0]):
        s, e, f, d = defects[i, 0]
        start = tuple(approx[s][0])
        end = tuple(approx[e][0])
        far = tuple(approx[f][0])
        pt = (100, 180)

        a = math.sqrt((end[0] - start[0]) ** 2 + (end[1] - start[1]) ** 2)
        b = math.sqrt((far[0] - start[0]) ** 2 + (far[1] - start[1]) ** 2)
        c = math.sqrt((end[0] - far[0]) ** 2 + (end[1] - far[1]) ** 2)
        s = (a + b + c) / 2
        ar = math.sqrt(s * (s - a) * (s - b) * (s - c))

        d = (2 * ar) / a
        angle = math.acos((b ** 2 + c ** 2 - a ** 2) / (2 * b * c)) * 57

        if angle <= 90 and d > 20:
            number_of_defects += 1
            cv2.circle(area_of_interest, far, 3, [255, 0, 0], -1)

        cv2.line(area_of_interest, start, end, [255, 0, 0], 2)

    number_of_defects += 1

    return number_of_defects, area_of_interest


def predict_gesture(number_of_defects, area_ratio, contour_area):

    if number_of_defects == 1:
        if contour_area < 2000:
            return -1
        else:
            if area_ratio < 12:
                return 0
            else:
                return 1
    elif number_of_defects == 2:
        return 2
    elif number_of_defects == 3:
        return 3
    elif number_of_defects == 4:
        return 4
    elif number_of_defects == 5:
        return 5
    else:
        return 6


def guess_gestures(gesture_type, gesture_array, pos):
    pos %= 19
    gesture_array[pos] = gesture_type
    arr = [0]*10
    for i in gesture_array:
        arr[gesture_array[i]+1] += 1;
        if(arr[gesture_array[i]+1]>12):
            return i;
    return -1
    # gesture_list = gesture_array.tolist()
    # # print(gesture_list)
    # return max(set(gesture_list), key = gesture_list.count)
