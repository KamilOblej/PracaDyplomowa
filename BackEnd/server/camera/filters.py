import django_filters
from django_filters import DateRangeFilter

from .models import Photo

class PhotosFilter(django_filters.FilterSet):
    start_date = DateRangeFilter(field_name='date_taken')


    class Meta:
        model = Photo
        fields = '__all__'
        exclude = ['image', 'name', 'date_taken']