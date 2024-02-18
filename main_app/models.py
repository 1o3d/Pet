from django.db import models


class historicalModels(models.Model):
    id = models.IntegerField()
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    community = models.CharField(max_length=255)
    contruction_yr = models.IntegerField()
    typology = models.CharField(max_length=255)
    orig_use_ty = models.CharField(max_length=255)
    architect = models.CharField(max_length=255, default='', blank=True)
    architecture_style = models.CharField(max_length=255, default='', blank=True)
    development_era = models.CharField(max_length=255, default='', blank=True)
    significance_summ = models.CharField(max_length=255, default='', blank=True)
    integrity_stmt = models.CharField(max_length=255, default='', blank=True)
    pic_url = models.URLField(max_length=255, null = True, default = '', blank = True)
