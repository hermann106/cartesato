import os
from django.contrib.gis.utils import LayerMapping
from .models import Structures

structures_mapping = {
    'etablis_id' : 'ETABLIS_ID',
    'nom_fs' : 'NOM_FS',
    'localite' : 'LOCALITE',
    'region' : 'REGION',
    'district' : 'DISTRICT',
    'type' : 'TYPE',
    'nature' : 'NATURE',
    'zone' : 'ZONE',
    'nb_village' : 'NB_VILLAGE',
    'altitude' : 'ALTITUDE',
    'latitude' : 'LATITUDE',
    'longitude' : 'LONGITUDE',
    'geom' : 'POINT',
}

structures_path = os.path.abspath(
    os.path.join(os.path.dirname(__file__), 'data', 'donnees_casato3.shp'),
)

def run(verbose=True):
    lm = LayerMapping(
        Structures, structures_path, structures_mapping,
        transform=False, encoding='utf-8',
    )
    lm.save(strict=True, verbose=verbose)