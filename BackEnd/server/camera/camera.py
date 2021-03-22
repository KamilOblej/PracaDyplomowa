import cv2
import numpy as np
from pylepton import Lepton
import copy
from . script import face_recognition, save_image
from time import sleep

class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)
        sleep(2)

    def __del__(self):
        self.video.release()

    def get_frame(self):
        success, image = self.video.read()
        try:
            
            face_recognition(image)
        except:
            print('error')
            sleep(5)
            success, image = self.video.read()
            face_recognition(image)
        # save_image(image)
        ret, jpeg = cv2.imencode('.jpg', image)
        # except:
        #     jpeg = np.zeros((512, 512, 1), dtype = "uint8")
        return jpeg.tobytes()

    def get_frame_manual(self):
        success, image = self.video.read()
        save_image(image)
        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()
