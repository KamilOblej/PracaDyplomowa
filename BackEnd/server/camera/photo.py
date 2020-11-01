from picamera import PiCamera
from time import sleep
from datetime import datetime, date
# from dbinsert import insert
from . getTemperature import getTemperature
from . thermoSnapshot import thermo

from . models import Photo, Temperature


def takePhoto(camera, path, format):
    now = datetime.now()
    today = date.today()
    today = today.strftime("%d-%m-%Y_")

    current_time = now.strftime("%H_%M_%S")

    fileName = ''+today+current_time
    camera.capture(path + fileName + format)
    print('Photo taken at [' + fileName + ']')


# function take photos from vision and thermal camera
def takePhotos(camera, path, format, path2):
    now = datetime.now()
    today = date.today()
    today = today.strftime("%d-%m-%Y_")
    current_time = now.strftime("%H_%M_%S")

    file_name = ''+today + current_time
    pathPhoto = path + file_name
    pathTermo = path2

    thermo(pathTermo, 'thermo' + file_name, format)
    camera.capture(pathPhoto + format)

    photo = Photo()
    photo.name = file_name
    photo.image = file_name + format
    photo.save()

    print('Photos taken at [' + file_name + ']')
    t = getTemperature()

    temperature = Temperature()
    temperature.temperature1 = t[0]
    temperature.temperature2 = t[1]
    temperature.save()
    # print ('Temperatures:', t[0], ';', t[1])

    # insertion pictures in databese with data from temp sensors
    # insert(path + fileName + format, str(t[0]), str(t[1]), path2 + fileName + format)
