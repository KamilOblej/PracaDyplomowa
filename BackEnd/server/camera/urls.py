from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    url(r'^/(?P<stream_path>(.*?))/$', views.dynamic_stream, name="videostream"),
    url(r'^stream/$', views.indexscreen, name='stream'),
    path('webcam_feed', views.webcam_feed, name='webcam_feed'),
    # path('thermal_feed', views.thermal_feed, name='thermal_feed'),
    path('got_to_history/', views.history_first, name='history_first'),
    url(r'^history/$',views.photos_history, name='history'),
    # path('history/',views.photos_history, name='history'),
]
