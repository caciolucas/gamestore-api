from django.db import models
from django.contrib.auth.models import User

from catalog.models import Game
from common.models import BaseModel


# Create your models here.

class Cart(BaseModel):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='cart')
    games = models.ManyToManyField(Game, related_name='carts')

    def __str__(self):
        return f'{self.user.username} - {self.games.count()} games'

    def total(self):
        subtotal = self.games.aggregate(models.Sum('price'))['price__sum']
        if subtotal >= 250:
            return subtotal
        else:
            return subtotal + 10 * self.games.count()

