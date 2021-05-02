import cv2
import device_information
import gesture_detection
import numpy as np
import interface
import pre_processing
import time


if __name__ == '__main__':
    # try:
    screen_width, screen_height = device_information.get_device_information()
    lower_skin_bound, upper_skin_bound = np.array([0, 10, 60]), np.array([20, 150, 255])
    camera = cv2.VideoCapture(0)

    prev_gestures = np.array([-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1])
    pos = 0

    while True:
        ret, frame = camera.read()
        frame = cv2.flip(frame, 1)

        area_of_interest, x1, y1, x2, y2 = pre_processing.get_area_of_interest(frame)
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)

        contour = pre_processing.get_contour(area_of_interest, lower_skin_bound, upper_skin_bound, screen_width, screen_height)
        defects, contour_area, area_ratio, approx = gesture_detection.get_defects(contour)

        number_of_defects, area_of_interest = gesture_detection.count_defects(defects, approx, area_of_interest)
        gesture_type = gesture_detection.predict_gesture(number_of_defects, area_ratio, contour_area)

        interface.display_frame(area_of_interest, screen_width, screen_height)
        interface.show_gesture(gesture_type, screen_width, screen_height)

        gesture_type = gesture_detection.guess_gestures(gesture_type, prev_gestures, pos)
        pos += 1

        print('gesture: ', gesture_type)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        time.sleep(0.2)

    cv2.destroyAllWindows()
    camera.release()

    # except:
    #     pass
