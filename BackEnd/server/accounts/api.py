from rest_framework import generics, permissions, mixins
from rest_framework.response import Response
from .serializers import RegisterSerializer, UserSerializer
from camera.models import Photo, Thermo, Temperature
from .serializers import PhotoSerializer, ThermoSerializer, TemperatureSerializer
from django.contrib.auth.models import User

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


class GetData(generics.GenericAPIView):
    def get(self, request, *args, **kwargs):
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
