from django.db import models


class Item(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.IntegerField()
    datetime = models.DateTimeField()
    server = models.CharField(max_length=100, default='')

    def __str__(self):
        return self.name
