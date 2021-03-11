from django.shortcuts import render, redirect
from picamera import PiCamera
from . getTemperature import getTemperature
import numpy as np
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
import math
from . camera import VideoCamera
from . thermoSnapshot import thermo
from . models import Photo, Thermo, Temperature
from .filters import PhotosFilter


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

def gen_manual(camera):
    while True:
        frame = camera.get_frame_manual()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')



def webcam_feed(request):
    return StreamingHttpResponse(gen(VideoCamera()),
                                 content_type='multipart/x-mixed-replace; boundary=frame')

def webcam_feed_manual(request):
    return StreamingHttpResponse(gen_manual(VideoCamera()),
                                 content_type='multipart/x-mixed-replace; boundary=frame')

# def thermal_feed(request):
#     return StreamingHttpResponse(gen(ThermalCamera()),
#                                  content_type='multipart/x-mixed-replace; boundary=frame')


def indexscreen(request):
    if request.user.is_authenticated:
        temperatures = getTemperature()
        context = {
            'temperatures': temperatures
        }
        template = "stream.html"
        return render(request, template, context)
    else:
        return redirect('http://82.145.73.141')

def indexscreen_manual(request):
    temperatures = getTemperature()
    context = {
        'temperatures': temperatures
    }
    template = "stream_manual.html"
    return render(request, template, context)


@gzip.gzip_page
def dynamic_stream(request, stream_path="video"):
    try:
        return StreamingHttpResponse(get_frame(), content_type="multipart/x-mixed-replace;boundary=frame")
    except:
        return "error"

def dynamic_stream_manual(request, stream_path="video"):
    try:
        return StreamingHttpResponse(get_frame_manual(), content_type="multipart/x-mixed-replace;boundary=frame")
    except:
        return "error"


def history_first(request):
    return redirect('/history/?page=1&start_date=today')

def photos_history(request):


    # photos = Photo.objects.all()
    # items = photos.count()

    # temperatures = Temperature.objects.all()
    title = 'Photos from database:'
    message = ''

    # my_filter = PhotosFilter(request.GET, queryset=photos)
    my_filter = PhotosFilter(request.GET, queryset=Photo.objects.all())
    photos = my_filter.qs
    # print(photos.count())
    items = Photo.objects.all().count()

    offset = 30
    
    try:
        page_nr = int(request.GET['page'])
    except:
        page_nr = 1
    # if int(request.GET['page']):
    #     page_nr = int(request.GET['page'])


    if page_nr > 1:
        start = int(request.GET['page']) * offset - offset
    else:
        start = 0
    
    stop = start + offset

    if stop > items:
        stop = items

    photos2 = photos[start:stop]

    data_set = []

    for photo in photos2:
        data = {
            'photo' : photo,
            'temperature' : Temperature.objects.get(pk=photo.pk),
            'thermo' : Thermo.objects.get(pk=photo.pk)
        }
        data_set.append(data)
        # print(data['temperature'])

    if not data_set:
        message = 'No data for this date period'
    else:
        message =  str(photos.count()) + ' elements found'

    
    pages = []

    for page in  range( 1,math.ceil(photos.count() / offset) + 1):
        pages.append(page)


    template = "history.html"
    context = {
        'title' : title,
        'message' : message,
        'data_set' : data_set,
        'pages' : pages,
        'my_filter' : my_filter,
    }


    return render(request, template, context)




