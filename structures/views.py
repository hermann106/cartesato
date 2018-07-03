from django.shortcuts import render
from django.core.serializers import serialize
from django.http import HttpResponse
from .models import *

# Create your views here.


def structures(request):
    structures_as_geojson = serialize("geojson", Structures.objects.all())
    return HttpResponse(structures_as_geojson, content_type="json")

