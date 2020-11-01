import glob
import cv2
from time import sleep
import datetime
import numpy as np


def save_image(image):
    file_format = '.jpg'
    now = datetime.datetime.now()
    file_name = 'img/foto' + \
        str(now.minute) + str(now.second) + str(now.microsecond) + file_format
    cv2.imwrite(file_name, image)


def face_recognition(item):
    face_cascade = cv2.CascadeClassifier(
        'streamdjango/haarcascade_frontalface_default.xml')
    # img = cv2.imread(item)
    gray = cv2.cvtColor(item, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    for (x, y, w, h) in faces:
        cv2.rectangle(item, (x, y), (x + w, y + h), (0, 255, 255), 2)

    found = len(faces)

    return item
