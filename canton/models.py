from django.db import models

# Create your models here.

# This is an auto-generated Django model module created by ogrinspect.

from django.contrib.gis.db import models

class Cantons(models.Model):
    objectid = models.IntegerField()
    nm_canton = models.CharField(max_length=27)
    prefecture = models.CharField(max_length=12)
    region = models.CharField(max_length=8)
    nbre_cant = models.FloatField()
    geom = models.MultiPolygonField()

    def __str__(self):
        return self.nm_canton

# Auto-generated `LayerMapping` dictionary for Cantons model
cantons_mapping = {
    'objectid' : 'OBJECTID',
    'nm_canton' : 'NM_CANTON',
    'prefecture' : 'PREFECTURE',
    'region' : 'REGION',
    'nbre_cant' : 'NBRE_CANT',
    'geom' : 'MULTIPOLYGON',
}
