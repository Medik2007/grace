from django.db import models
from django.contrib.auth.models import AbstractUser
from dress.models import Dress, DressColor, DressModel, DressSize

import uuid

def create_id(): return str(uuid.uuid4().hex)[:12]


class User(AbstractUser):
    name = models.CharField(max_length=64)
    phone = models.CharField(max_length=10)
    is_verified = models.BooleanField(default=False) #type:ignore
    verification_token = models.CharField(max_length=64, null=True)
    verification_sent = models.DateTimeField(null=True)
    date = models.DateField(auto_now_add=True)


class Delivery(models.Model):
    id = models.CharField(max_length=12, primary_key=True, editable=False, default=create_id)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='deliveries', null=True)
    adress = models.CharField(max_length=512, null=True)
    date = models.DateField(auto_now_add=True)
    # 1 - Delivery made; 2 - Orders accepted; 3 - Orders produced; 4 - Orders delivered; 0 - Order canceled
    state = models.IntegerField(default=1) #type:ignore

    def full_price(self):
        result = 0
        for i in self.orders: #type:ignore
            result += i.full_price()
        return result

    def __str__(self):
        return f"Заказ от {self.date}: {self.user.name}"


class Order(models.Model):
    id = models.CharField(max_length=12, primary_key=True, editable=False, default=create_id)
    delivery = models.ForeignKey(Delivery, on_delete=models.CASCADE, related_name='orders')
    dress = models.ForeignKey(Dress, on_delete=models.SET_NULL, null=True, related_name='orders')
    color = models.ForeignKey(DressColor, on_delete=models.SET_NULL, null=True, related_name='orders')
    size = models.ForeignKey(DressSize, on_delete=models.SET_NULL, null=True, related_name='orders')
    model = models.ForeignKey(DressModel, on_delete=models.SET_NULL, null=True, related_name='orders')
    amount = models.IntegerField()

    def full_price(self):
        return self.model.price * self.amount #type:ignore

    def __str__(self):
        return ''
