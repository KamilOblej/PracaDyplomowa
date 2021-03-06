from django.db import models
# from matrix_field import MatrixField

# Create your models here.



class Photo(models.Model):

    name = models.CharField(max_length=200)
    image = models.ImageField()
    date_taken = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.pk)+ ' ) ' +str(self.name)


class Thermo(models.Model):

    name = models.CharField(max_length=200)
    image = models.ImageField()
    date_taken = models.DateTimeField(auto_now_add=True, null=True)
    # matrix1 = MatrixField(datatype='float', dimensions=(3, 2))
    matrix = models.TextField(blank=True, null=True)
    # raw_matrix = models.ma

    def __str__(self):
        return str(self.pk)+ ' ) ' +str(self.name)


class Temperature(models.Model):

    temperature1 = models.CharField(max_length=20)
    temperature2 = models.CharField(max_length=20)
    date_taken = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return str(self.pk)+ ' ) ' +str(self.temperature1)+ ' ' +str(self.temperature2) 
