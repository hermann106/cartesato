from django.contrib import admin
from structures.models import *
from django.contrib.gis.admin import *

# Register your models here.
admin.site.register(Structures, OSMGeoAdmin)
