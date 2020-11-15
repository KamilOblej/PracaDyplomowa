from django.contrib import admin

from . models import Photo, Thermo, Temperature
# Register your models here.

admin.site.register(Photo)
admin.site.register(Thermo)
admin.site.register(Temperature)
