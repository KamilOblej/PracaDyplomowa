import glob
import cv2
from time import sleep
import datetime
import copy

import numpy as np
from . models import Photo, Temperature
from . getTemperature import getTemperature
from .thermoSnapshot import thermo


def save_image(image):
    now = datetime.datetime.now()
    today = datetime.date.today()
    today = today.strftime("%d-%m-%Y_")
    current_time = now.strftime("%H_%M_%S")
    file_path = 'static/images/'
    file_format = '.jpg'
    file_name = ''+today + current_time
    pathPhoto = file_path + file_name + file_format

    # now = datetime.datetime.now()
    # file_name = 'img/foto' + \
    #     str(now.minute) + str(now.second) + str(now.microsecond) + file_format
    # cv2.imwrite(file_name, image)
    cv2.imwrite(pathPhoto, image)

    photo = Photo()
    photo.name = file_name
    photo.image = file_name + file_format
    photo.save()

    thermo(file_path, 'thermo' + file_name, file_format)

    print('Photo taken at [' + file_name + ']')


def save_temperature():
    t = getTemperature()

    temperature = Temperature()
    temperature.temperature1 = t[0]
    temperature.temperature2 = t[1]
    temperature.save()


def save_thermo():
    pass


def face_recognition(item):
    face_cascade = cv2.CascadeClassifier(
        'camera/haarcascade_frontalface_default.xml')
    gray = cv2.cvtColor(item, cv2.COLOR_BGR2GRAY)
    image = copy.copy(item)

    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    for (x, y, w, h) in faces:
        cv2.rectangle(item, (x, y), (x + w, y + h), (0, 255, 255), 2)

    found = len(faces)
    if found != 0:
        save_image(image)
        save_temperature()

    return item