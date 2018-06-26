from django.db import models

# Create your models here.

# This is an auto-generated Django model module created by ogrinspect.
from django.contrib.gis.db import models

class Structures(models.Model):
    etablis_id = models.CharField(max_length=254)
    nom_fs = models.CharField(max_length=254)
    localite = models.CharField(max_length=254)
    region = models.CharField(max_length=254)
    district = models.CharField(max_length=254)
    type = models.CharField(max_length=254)
    nature = models.CharField(max_length=254)
    zone = models.CharField(max_length=254)
    nb_village = models.BigIntegerField()
    altitude = models.FloatField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    geom = models.PointField()

    def __str__(self):
        return self.nom_fs

# Auto-generated `LayerMapping` dictionary for Structures model
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

