from django.db import models


class historicalModels(models.Model):
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

    def __str__(self):
        return self.name

class Quiz(models.Model):
    ZODIAC_CHOICES = (
        ('Aries', 'Aries'),
        ('Taurus', 'Taurus'),
        ('Gemini', 'Gemini'),
        ('Cancer', 'Cancer'),
        ('Leo', 'Leo'),
        ('Virgo', 'Virgo'),
        ('Libra', 'Libra'),
        ('Scorpio', 'Scorpio'),
        ('Sagittarius', 'Sagittarius'),
        ('Capricorn', 'Capricorn'),
        ('Aquarius', 'Aquarius'),
        ('Pisces', 'Pisces'),
    )
    zodiac = models.CharField(max_length=20, choices=ZODIAC_CHOICES)

    HORROR_CHOICES = (
        ('Cemetery', 'Cemetery'),
        ('Warehouse', 'Warehouse'),
        ('Hospital', 'Hospital'),
        ('Factory', 'Factory'),
        ('Hotel', 'Hotel'),
        ('Grocery Store', 'Grocery Store'),
        ('None', 'None'),
    )
    horror = models.CharField(max_length=20, choices=HORROR_CHOICES)

    bridges = models.BooleanField(default=False)

    PROFESSION_CHOICES = (
        ('Baker', 'Baker'),
        ('Civil Engineer', 'Civil Engineer'),
        ('Farmer', 'Farmer'),
        ('Priest', 'Priest'),
        ('Librarian', 'Librarian'),
        ('Teacher', 'Teacher'),
        ('None', 'None'),
    )
    profession = models.CharField(max_length=20, choices=PROFESSION_CHOICES)
    def __str__(self):
        return self.ZODIAC_CHOICES
