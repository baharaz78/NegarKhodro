from django.db import models

from animals import AnimalType


class Animal(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    species = models.CharField(max_length=16, choices=AnimalType.choices)
    name = models.CharField(max_length=64)

    def __str__(self):
        return f"{self.name} [{self.species}]"
