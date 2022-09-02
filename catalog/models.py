from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.utils.text import slugify
from django.urls import reverse


# Create your models here.

class Brend(models.Model):
    name = models.CharField(max_length=20)
    image = models.FileField(upload_to='gallery_auto', default=None)

    def __str__(self):
        return f'{self.name}'


class Auto(models.Model):
    WHT = 'WHT'
    GRY = 'GRY'
    BLE = 'BLE'
    RED = 'RED'
    BLK = 'BLK'

    COLOR_CHOICES = [
        (WHT, 'Белый'),
        (GRY, 'Серый'),
        (BLE, 'Синий'),
        (RED, 'Красный'),
        (BLK, 'Чёрный'),
    ]
    name = models.CharField(max_length=50)
    year = models.IntegerField(null=True, blank=True, validators=[MinValueValidator(1950), MaxValueValidator(2023)])
    mileage = models.IntegerField(null=True, blank=True, validators=[MinValueValidator(0), MaxValueValidator(2000000)])
    color = models.CharField(max_length=3, choices=COLOR_CHOICES, default=BLK)
    brend = models.ForeignKey(Brend, on_delete=models.CASCADE, null=True, related_name='autos')
    image = models.FileField(upload_to='gallery_auto')
    price = models.IntegerField(null=True, blank=True, validators=[MinValueValidator(0), MaxValueValidator(100000000)])
    owners = models.IntegerField(null=True, blank=True, validators=[MinValueValidator(1), MaxValueValidator(15)])
    slug_auto = models.SlugField(default='', null=False, db_index=True)

    def get_url(self):
        return reverse('one_car', args=[self.slug_auto])

    def __str__(self):
        return f'{self.name}-{self.year}'
