from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db.models import Model, DateTimeField, CharField, ImageField, SlugField, TextField, FloatField, ForeignKey, \
    CASCADE, IntegerField, TextChoices
from django.utils.text import slugify


class Category(Model):
    name = CharField(max_length=500)

    def __str__(self):
        return self.name


class Product(Model):
    class Color(TextChoices):
        BLACK = "black", 'Black'
        GRAY = "gray", 'Gray'
        DARK_GREEN = "dark green", 'Dark green'
        BLUE = "blue", 'Blue'

    name = CharField(max_length=255)
    color = CharField(max_length=50, choices=Color.choices, default=Color.BLACK)
    description = TextField()
    price = FloatField()
    quantity = IntegerField()
    category = ForeignKey('apps.Category', CASCADE, related_name='products')
    image = ImageField(upload_to='products/')
    size = IntegerField()

    def __str__(self):
        return self.name


class Profile(Model):
    first_name = CharField(max_length=255)
    last_name = CharField(max_length=255)
    phone = FloatField()
    mobile_number = FloatField()
    email = CharField(max_length=255)
    skype = CharField(max_length=255)
