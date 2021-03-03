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

    cv2.imwrite(pathPhoto, image)

    photo = Photo()
    photo.name = file_name
    photo.image = file_name + file_format
    photo.save()
    print("Photo stored in database")
    thermo(file_path, 'thermo' + file_name, file_format)
    save_temperature()
    print("Temperature stored")

    # print('Photo taken at [' + photo.date_taken + ']')


def save_temperature():
    try:
        t = getTemperature()
    except:
         t = [0.0, 0.0]

    temperature = Temperature()
    temperature.temperature1 = t[0]
    temperature.temperature2 = t[1]
    temperature.save()




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

    return item
