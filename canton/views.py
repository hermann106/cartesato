from django.shortcuts import render
from django.core.serializers import serialize
from django.http import HttpResponse
from .models import *

from django.core.cache import cache
# Create your views here.


def cantons(request):
    redis_key = "cantons"
    cantons_as_geojson = cache.get(redis_key)
    if not cantons_as_geojson:
        cantons_as_geojson = serialize("geojson", Cantons.objects.all())
        cache.set(redis_key, cantons_as_geojson)
    return HttpResponse(cantons_as_geojson, content_type="json")
