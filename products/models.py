from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=255)
    length = models.FloatField()
    width = models.FloatField()
    height = models.FloatField()
    weight = models.FloatField()

    def __str__(self):
        return self.name