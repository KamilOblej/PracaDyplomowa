import django_filters
from django_filters import DateRangeFilter, DateTimeFromToRangeFilter

from .models import Photo

class PhotosFilter(django_filters.FilterSet):
    start_date = DateTimeFromToRangeFilter(field_name='date_taken')


    class Meta:
        model = Photo
        fields = '__all__'
        exclude = ['image', 'name', 'date_taken']