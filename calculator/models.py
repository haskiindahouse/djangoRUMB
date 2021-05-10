from django.db import models

DATUMS = (('0', 'WGS84'), ('1', 'Пулково 42'))


class Point(models.Model):
    name = models.CharField(max_length=10, default='NaN')
    x = models.CharField(max_length=50, default='NaN')
    y = models.CharField(max_length=50, default='NaN')
    z = models.CharField(max_length=50, default='NaN')
    longitude = models.CharField(max_length=50, default='NaN')
    latitude = models.CharField(max_length=50, default='NaN')

    datum = models.CharField(max_length=10, choices=DATUMS, default="0")
