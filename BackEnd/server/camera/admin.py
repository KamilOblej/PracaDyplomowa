from django.contrib import admin

from .models import Data, Photo, Thermo, Temperature
# Register your models here.

admin.site.register(Data)
admin.site.register(Photo)
admin.site.register(Thermo)
admin.site.register(Temperature)
