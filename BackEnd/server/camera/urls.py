from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('take_one_photo/', views.take_one_photo, name='take_one_photo'),
    path('take_photos_sequence/', views.take_photos_sequence,
         name='take_photos_sequence'),
    path('get_data', views.get_data, name='get_data'),
    # path('get_data/take_photos_sequence', views.take_photos_sequence, name='get_data/take_photos_sequence'),
    path('take_one_photo/test/', views.test, name='test'),
    url(r'^/(?P<stream_path>(.*?))/$', views.dynamic_stream, name="videostream"),
    url(r'^stream/$', views.indexscreen, name='stream'),
    path('webcam_feed', views.webcam_feed, name='webcam_feed'),
    path('thermal_feed', views.thermal_feed, name='thermal_feed'),
    path('got_to_history/', views.history_first, name='history_first'),
    url(r'^history/$',views.photos_history, name='history'),
]
