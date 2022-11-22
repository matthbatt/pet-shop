from django.conf import settings
from django.db import models
from django.utils import timezone
from django.shortcuts import get_object_or_404


class Equipement(models.Model):
    id_equip = models.CharField(max_length=100, primary_key=True)
    disponibilite = models.CharField(max_length=20)
    photo = models.ImageField( upload_to ="images/")

    def __str__(self):
        return self.id_equip


class Animal(models.Model):
    id_animal = models.CharField(max_length=100, primary_key=True)
    etat = models.CharField(max_length=20)
    type = models.CharField(max_length=20)
    race = models.CharField(max_length=20)
    photo = models.ImageField( upload_to ="images/")
    lieu = models.ForeignKey(Equipement, on_delete=models.CASCADE)

    def __str__(self):
        return self.id_animal




