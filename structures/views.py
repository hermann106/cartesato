from django.shortcuts import render
from django.core.serializers import serialize
from django.http import HttpResponse
from .models import *

from django.core.cache import cache
# Create your views here.


def structures(request):
    redis_key = "structures"
    structures_as_geojson = cache.get(redis_key)
    if not structures_as_geojson:
        structures_as_geojson = serialize("geojson", Structures.objects.all())
        cache.set(redis_key, structures_as_geojson)
    return HttpResponse(structures_as_geojson, content_type="json")

