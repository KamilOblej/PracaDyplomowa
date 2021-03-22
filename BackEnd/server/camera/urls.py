from django.urls import path, include
from django.conf.urls import url

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    url(r'^/(?P<stream_path>(.*?))/$', views.dynamic_stream, name="videostream"),
    url(r'^/(?P<stream_path>(.*?))/$', views.dynamic_stream_manual, name="videostream_manual"),
    url(r'^stream/$', views.indexscreen, name='stream'),
    url(r'^stream_manual/$', views.indexscreen_manual, name='stream_manual'),
    path('webcam_feed', views.webcam_feed, name='webcam_feed'),
    path('webcam_feed_manual', views.webcam_feed_manual, name='webcam_feed_manual'),
    # path('thermal_feed', views.thermal_feed, name='thermal_feed'),
    path('got_to_history/', views.history_first, name='history_first'),
    url(r'^history/$',views.photos_history, name='history'),
    path('processing/', views.go_to_processing, name='processing')
    # path('history/',views.photos_history, name='history'),
]
