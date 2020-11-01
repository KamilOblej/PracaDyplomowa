from django.db import models

# Create your models here.


class Data(models.Model):

    class Meta:
        verbose_name_plural = 'Data'

    name = models.CharField(max_length=200)
    photo = models.ImageField()
    thermo = models.ImageField()
    temperature1 = models.CharField(max_length=20)
    temperature2 = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Photo(models.Model):

    name = models.CharField(max_length=200)
    image = models.ImageField()

    def __str__(self):
        return self.name


class Thermo(models.Model):

    name = models.CharField(max_length=200)
    image = models.ImageField()

    def __str__(self):
        return self.name


class Temperature(models.Model):

    temperature1 = models.CharField(max_length=20)
    temperature2 = models.CharField(max_length=20)

    def __str__(self):
        return self.temperature1, self.temperature2
