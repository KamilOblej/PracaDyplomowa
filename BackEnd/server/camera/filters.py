import django_filters
from django_filters import DateRangeFilter, DateTimeFromToRangeFilter

from .models import Photo, Thermo, Temperature

class PhotosFilter(django_filters.FilterSet):
    start_date = DateTimeFromToRangeFilter(field_name='date_taken')

    class Meta:
        model = Photo
        fields = '__all__'
        exclude = ['image', 'name', 'date_taken']

class ThermosFilter(django_filters.FilterSet):
    start_date = DateTimeFromToRangeFilter(field_name='date_taken')

    class Meta:
        model = Thermo
        fields = '__all__'
        exclude = ['image', 'name', 'date_taken']

class TemperaturesFilter(django_filters.FilterSet):
    start_date = DateTimeFromToRangeFilter(field_name='date_taken')

    class Meta:
        model = Temperature
        fields = '__all__'