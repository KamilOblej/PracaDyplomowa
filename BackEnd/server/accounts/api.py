from rest_framework import generics, permissions, mixins
from rest_framework.response import Response
from .serializers import RegisterSerializer, UserSerializer
from camera.models import Photo, Thermo, Temperature
from .serializers import PhotoSerializer, ThermoSerializer, TemperatureSerializer
from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from camera.filters import PhotosFilter, ThermosFilter, TemperaturesFilter

#Register API
class RegisterApi(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    def post(self, request, *args,  **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user,    context=self.get_serializer_context()).data,
            "message": "User Created Successfully.  Now perform Login to get your token",
        })

class SimpleApI(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)


class GetData(generics.GenericAPIView):
    def get(self, request, *args, **kwargs):
        print(request.user)
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
        return Response(data)

class GetDataByDate(generics.GenericAPIView):
    def get(self, request, *args, **kwargs):
        photo_filter = PhotosFilter(request.GET, queryset=Photo.objects.all())
        photos = photo_filter.qs

        thermo_filter = ThermosFilter(request.GET, queryset=Thermo.objects.all())
        thermos = thermo_filter.qs

        temperature_filter = TemperaturesFilter(request.GET, queryset=Temperature.objects.all())
        temperatures = temperature_filter.qs

        photos_serializer = PhotoSerializer(photos, many=True)
        thermo_serializer = ThermoSerializer(thermos, many=True)
        temperature_serializer = TemperatureSerializer(temperatures, many=True)

        data ={
            "photos" : photos_serializer.data,
            "thermos" : thermo_serializer.data,
            "temperatures" : temperature_serializer.data,
        }
        return Response(data)
        