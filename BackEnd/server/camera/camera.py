import cv2
import numpy as np
from pylepton import Lepton
import copy
from . script import face_recognition

face_cascade = cv2.CascadeClassifier(
    'helloDjango/haarcascade_frontalface_default.xml')


class VideoCamera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)

    def __del__(self):
        self.video.release()

    def get_frame(self):
        success, image = self.video.read()
        face_recognition(image)

        # gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        # faces_detected = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)
        # for (x, y, w, h) in faces_detected:
        # 	cv2.rectangle(image, pt1=(x, y), pt2=(x + w, y + h), color=(255, 0, 0), thickness=2)
        # frame_flip = cv2.flip(image,1)
        ret, jpeg = cv2.imencode('.jpg', image)
        return jpeg.tobytes()
