import cv2
import pyautogui

import actions
import device_information
import gesture_detection
import keypad
import numpy as np
import interface
import pre_processing
import time
from PyQt5.QtCore import QObject, QThread, pyqtSignal


class Worker(QObject):
    finished = pyqtSignal()
    progress = pyqtSignal(int)

    def run(self):
        screen_width, screen_height = device_information.get_device_information()
        lower_skin_bound, upper_skin_bound = np.array([0, 20, 70]), np.array([20, 255, 255])
        camera = cv2.VideoCapture(0)
        prev_gestures = np.array([-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1])
        pos = 0
        prev_timestamp = time.time()
        prev_action_timestamp = time.time()
        global show_keypad
        # self.thread.start()
        # keypad.open_keypad()

        while True:
            ret, frame = camera.read()
            frame = cv2.flip(frame, 1)

            area_of_interest, x1, y1, x2, y2 = pre_processing.get_area_of_interest(frame)
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)

            contour = pre_processing.get_contour(area_of_interest, lower_skin_bound, upper_skin_bound, screen_width,
                                                 screen_height)
            defects, contour_area, area_ratio, approx = gesture_detection.get_defects(contour)

            number_of_defects, area_of_interest = gesture_detection.count_defects(defects, approx, area_of_interest)
            gesture_type = gesture_detection.predict_gesture(number_of_defects, area_ratio, contour_area)

            interface.display_frame(area_of_interest, screen_width, screen_height)
            gesture_type = gesture_detection.guess_gestures(gesture_type, prev_gestures, pos)
            if gesture_type == 3:
                print('gesture 3')
                show_keypad = not show_keypad
            prev_timestamp = interface.show_gesture(gesture_type, screen_width, screen_height, prev_timestamp)
            prev_action_timestamp = actions.perform_action(gesture_type, prev_action_timestamp)
            pos += 1
            # print('gesture: ', gesture_type)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

            time.sleep(0.20)

        cv2.destroyAllWindows()
        camera.release()
        # except:
        #     pass
        self.progress.emit()
        self.finished.emit()


show_keypad = False

class Main():

    def __init__(self):
        self.thread = QThread()
        self.worker = Worker()
        self.worker.moveToThread(self.thread)
        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        # print('cp21')
        self.thread.finished.connect(self.thread.deleteLater)

    def main_fun(self):
        print('cp3')
        self.thread.start()
        print('cp212')
        opened_atleast_once = False
        while True:
            if show_keypad:
                opened_atleast_once = True
                pyautogui.click(150, 100)
                key_val = keypad.open_keypad()
                print(key_val)
            elif opened_atleast_once:
                keypad.close_keypad()
            time.sleep(1)
        # return key_val


if __name__ == '__main__':
    app = Main()
    app.main_fun()



