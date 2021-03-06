from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from camera.models import Photo, Thermo, Temperature
from .serializers import PhotoSerializer, ThermoSerializer, TemperatureSerializer
from camera.filters import PhotosFilter
# Create your views here.

def get_all_data(request):
    if request.method == 'GET':
        photos = Photo.objects.all()
        photos_serializer = PhotoSerializer(photos, many=True)

        thermos = Thermo.objects.all()
        thermos_serializer = ThermoSerializer(thermos, many=True)

        temperatures = Temperature.objects.all()
        temperatures_serializer = TemperatureSerializer(temperatures, many=True)

        data = {
            "photos" : photos_serializer.data,
            "thermos" : thermos_serializer.data,
            "temperatures" : temperatures_serializer.data,
        }
        return JsonResponse(data, safe=False)

def get_data_by_date(request):
    if request.method == 'GET':
        my_filter = PhotosFilter(request.GET, queryset=Photo.objects.filter(pk__lt=20))
        photos = my_filter.qs
        
        data_set = []

        for photo in photos:
            data = {
                'photo' : photo,
                'temperature' : Temperature.objects.get(pk=photo.pk),
                'thermo' : Thermo.objects.get(pk=photo.pk)
            }
            data_set.append(data)
    return JsonResponse(data_set, safe=False)