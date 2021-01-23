import cv2
import numpy as np
from pylepton import Lepton
import copy
from . script import face_recognition

class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)

    def __del__(self):
        self.video.release()

    def get_frame(self):
        success, image = self.video.read()
        face_recognition(image)
        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()
