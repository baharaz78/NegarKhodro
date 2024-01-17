from django.db.models import TextChoices


class AnimalType(TextChoices):
    CAT = "Cat", "cat"
    DOG = "Dog", "dog"
