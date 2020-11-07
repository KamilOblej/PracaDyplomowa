from django.shortcuts import render, redirect
from picamera import PiCamera
from . getTemperature import getTemperature
from . models import Data
import numpy as np
from datetime import datetime, date
import datetime
from time import sleep
from pylepton import Lepton
import copy
from django.shortcuts import render
from django.http import HttpResponse, StreamingHttpResponse, HttpResponseServerError
from django.views.decorators import gzip
import cv2
import time
from .script import face_recognition

from . photo import takePhotos

from . camera import VideoCamera
from . thermoSnapshot import thermo

from . models import Photo, Thermo
from django.core.paginator import Paginator


def index(request):
    temperatures = getTemperature()
    context = {
        'temperatures': temperatures
    }

    return render(request, 'index.html', context)


def get_frame():
    # camera = cv2.VideoCapture(0)
    # while True:
    #     _, img = camera.read()
    #     img2 = face_recognition(img)
    #     imgencode = cv2.imencode('.jpg', img2)[1]
    #     stringData = imgencode.tostring()
    #     yield (b'--frame\r\n'b'Content-Type: text/plain\r\n\r\n'+stringData+b'\r\n')
    # del(camera)
    while True:
        with Lepton() as l:
            a, _ = l.capture()

        cv2.normalize(a, a, 0, 65535, cv2.NORM_MINMAX)  # extend contrast
        np.right_shift(a, 8, a)  # fit data into 8 bits

        scale_percent = 400  # percent of original size
        width = int(a.shape[1] * scale_percent / 100)
        height = int(a.shape[0] * scale_percent / 100)
        dim = (width, height)
        resized = cv2.resize(a, dim, interpolation=cv2.INTER_AREA)
        a = copy.copy(resized)
        imgencode = cv2.imencode('.jpg', a)[1]
        stringData = imgencode.tostring()
        yield (b'--frame\r\n'b'Content-Type: text/plain\r\n\r\n'+stringData+b'\r\n')
    # del(camera)


def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


def webcam_feed(request):
    return StreamingHttpResponse(gen(VideoCamera()),
                                 content_type='multipart/x-mixed-replace; boundary=frame')


def thermal_feed(request):
    return StreamingHttpResponse(gen(ThermalCamera()),
                                 content_type='multipart/x-mixed-replace; boundary=frame')


def indexscreen(request):
    temperatures = getTemperature()
    context = {
        'temperatures': temperatures
    }
    template = "stream.html"
    return render(request, template, context)
    # try:
    #     template = "stream.html"
    #     return render(request, template, context)
    # except HttpResponseServerError:
    #     print("error")


@gzip.gzip_page
def dynamic_stream(request, stream_path="video"):
    try:
        return StreamingHttpResponse(get_frame(), content_type="multipart/x-mixed-replace;boundary=frame")
    except:
        return "error"


def take_one_photo(request):
    temperatures = getTemperature()
    camera = PiCamera()
    data = Data()

    # remove old preview from database
    preview = Data.objects.all()
    preview.delete()

    file_path = 'static/images/'
    file_name = 'preview.png'
    data.name = file_name
    data.temperature1 = temperatures[0]
    data.temperature2 = temperatures[1]
    print('Camera is working')
    camera.resolution = (1024, 768)
    camera.start_preview()
    camera.capture(file_path + file_name)
    data.photo = file_name
    print('Photo taken')
    data.save()

    d = Data.objects.all()
    context = {
        'pictures': d
    }
    # print(context['pictures'])
    camera.close()

    return render(request, 'photo_preview.html', context)


def get_data(request):
    # return render(request, 'get_data.html')
    return redirect('take_photos_sequence')
    # takePhotos()


def take_photos_sequence(request):

    # render()
    get_data(request)
    # remove old preview from database
    preview = Data.objects.all()
    preview.delete()

    now = datetime.datetime.now()
    print('START TIME ' + str(now.hour) + ':' +
          str(now.minute) + ':' + str(now.second))
    start_h = now.hour
    start_m = now.minute
    start_s = now.second

    WAIT_TIME = 1
    DELTA_TIME = 1

    file_path = 'static/images/'
    file_format = '.jpg'

    camera = PiCamera()
    camera.start_preview()

    # camera need some time to set exposition
    print('CAMERA CALIBRATION')
    sleep(WAIT_TIME)
    print('CAMERA CALIBRATED\n')

    current_second = now.second
    current_minute = now.minute
    current_hour = now.hour

    second_counter = 0
    seconds_in_minute = 10
    minutes = 1

    while (second_counter < minutes * seconds_in_minute):

        takePhotos(camera, file_path, file_format, file_path)
        second_counter = second_counter + 2
        print(second_counter)

    camera.close()

    message = 'System finished recording data'

    context = {
        'message': message,
    }
    return render(request, 'index.html', context)


def test(request):
    return redirect('take_one_photo')

def photos_history(request):
    photos = Photo.objects.all()
    thermos = Thermo.objects.all()
    message = 'Photos from database'
    items = len(photos) 

    paginator = Paginator(photos, 30)

    page = request.GET.get('page')

    photos = paginator.get_page(page)
    thermos = paginator.get_page(page)

    # ?page=2

    # photos = paginator.get_page(page)

    

    template = "history.html"
    context = {
        'message' : message,
        'items' : items,
        'photos' : photos,
        'thermos' : thermos, 
    }

    return render(request, template, context)
