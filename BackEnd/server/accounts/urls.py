from django.conf.urls import url
from django.urls import path, include
from .api import RegisterApi, GetData
from . import views
from .api import SimpleApI


urlpatterns = [
      path('api/register', RegisterApi.as_view()),
      path('api/get_data',views.get_all_data),
      path('api/photos', GetData.as_view()),
      path('api/hello', SimpleApI.as_view() ),
]