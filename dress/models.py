from django.db import models
import uuid

def create_id(): return str(uuid.uuid4().hex)[:12]


class Dress(models.Model):
    id = models.CharField(max_length=12, primary_key=True, editable=False, default=create_id)

    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=1000, blank=True)

    def __str__(self): #pyright:ignore
        return self.name


class DressColor(models.Model):
    id = models.CharField(max_length=12, primary_key=True, editable=False, default=create_id)
    dress = models.ForeignKey(Dress, on_delete=models.CASCADE, related_name='colors')

    img = models.ImageField(upload_to='images')
    name = models.CharField(max_length=100)

    def __str__(self): #pyright:ignore
        return self.name


class DressSize(models.Model):
    id = models.CharField(max_length=12, primary_key=True, editable=False, default=create_id)
    dress = models.ForeignKey(Dress, on_delete=models.CASCADE, related_name='sizes')

    size = models.IntegerField()

    def __str__(self): #pyright:ignore
        return str(self.size)


class DressModel(models.Model):
    id = models.CharField(max_length=12, primary_key=True, editable=False, default=create_id)
    dress = models.ForeignKey(Dress, on_delete=models.CASCADE, related_name='models')

    name = models.CharField(max_length=100)
    price = models.IntegerField()

    def __str__(self): #pyright:ignore
        return self.name
