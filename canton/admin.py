from django.contrib.gis import admin

# Register your models here.

from .models import *

admin.site.register(Cantons, admin.OSMGeoAdmin)
