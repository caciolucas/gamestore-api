from django.db import models

from common.models import BaseModel


# Create your models here.

class Game(BaseModel):
    name = models.CharField(max_length=100)
    score = models.IntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.FileField(upload_to='images/')

    def __str__(self):
        return self.name
