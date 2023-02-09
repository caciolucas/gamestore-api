from django.db import models
from django.contrib.auth.models import User

from common.models import BaseModel
from order.enums import PaymentMethod


# Create your models here.


class Order(BaseModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    payment_method = models.CharField(max_length=100, choices=PaymentMethod.choices())
    total = models.DecimalField(max_digits=6, decimal_places=2)
    # Could use the through parameter to a model to store the quantity of each game, but we only allow 1 copy of game per order
    items = models.ManyToManyField("catalog.Game", related_name='orders')

    def __str__(self):
        return f'{self.user.username} - {self.created_at}'

