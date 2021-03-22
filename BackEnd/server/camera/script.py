import glob
import cv2
from time import sleep
import datetime
import copy

import numpy as np
from . models import Photo, Temperature
from . getTemperature import getTemperature
from .thermoSnapshot import thermo, thermo_save
from server.settings import MEDIA_ROOT


def save_image(image):

    a = thermo()
    # print("Thermo stored in database " + str(datetime.datetime.now()))
    now = datetime.datetime.now()
    today = datetime.date.today()
    today = today.strftime("%d-%m-%Y_")
    current_time = now.strftime("%H_%M_%S")
    file_path = MEDIA_ROOT + '/'
    file_format = '.jpg'
    file_name = ''+today + current_time
    pathPhoto = file_path + file_name + file_format

    photo = Photo()
    photo.name = file_name
    photo.image = file_name + file_format
    
    # print("Photo stored in database " + str(datetime.datetime.now()))
    # print(pathPhoto)
    # print(cv2.imwrite(pathPhoto, image))
    if(cv2.imwrite(pathPhoto, image)):
        print('Photo saved successfully')
        thermo_save(file_path, 'thermo' + file_name, file_format,a)
        photo.save()
        save_temperature()
    # print("Temperature stored " + str(datetime.datetime.now()))
        print("Waiting 5s")
        sleep(5)
    print("--------------------------------\n")

    # print('Photo taken at [' + photo.date_taken + ']')


def save_temperature():
    temperature = Temperature()
    try:
        t = getTemperature()
    except:
        t = [0.0, 0.0]

    temperature.temperature1 = t[0]
    temperature.temperature2 = t[1]
    temperature.save()




def face_recognition(item):
    face_cascade = cv2.CascadeClassifier(
        'camera/haarcascade_frontalface_default.xml')
    gray = cv2.cvtColor(item, cv2.COLOR_BGR2GRAY)
    image = copy.copy(item)
    try:
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)

        for (x, y, w, h) in faces:
            cv2.rectangle(item, (x, y), (x + w, y + h), (0, 255, 255), 2)

        found = len(faces)
        if found != 0:
            save_image(image)

        return item
    except:
        return item
        
