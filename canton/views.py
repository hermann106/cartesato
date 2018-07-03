from django.shortcuts import render
from django.core.serializers import serialize
from django.http import HttpResponse
from .models import *
from django.views.decorators.cache import cache_page

# Create your views here.

def cantons(request):
    cantons_as_geojson = serialize("geojson", Cantons.objects.all())
    return HttpResponse(cantons_as_geojson, content_type="json")
