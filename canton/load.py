import os
from django.contrib.gis.utils import LayerMapping
from .models import *

cantons_mapping = {
    'objectid' : 'OBJECTID',
    'nm_canton' : 'NM_CANTON',
    'prefecture' : 'PREFECTURE',
    'region' : 'REGION',
    'nbre_cant' : 'NBRE_CANT',
    'geom' : 'MULTIPOLYGON',
}

cantons_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'data', 'limite canton togo.shp'),
)

def run(verbose=True):
    lm = LayerMapping(
        Cantons, cantons_path, cantons_mapping,
        transform=False, encoding='utf-8',
    )
    lm.save(strict=True, verbose=verbose)