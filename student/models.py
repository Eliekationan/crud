import email
from pyexpat import model
from tokenize import blank_re
from unicodedata import name
from django.db import models
from django.forms import SlugField
from setuptools import Require

# Create your models here.


class Student(models.Model) :
    name = models.CharField(max_length=20)
    slug = models.SlugField(max_length = 128)
    surname = models.CharField(max_length= 20)
    email = models.EmailField(unique=True)
    pic = models.ImageField(upload_to = "images", blank = True, null = True)
    

    def __str__(self):
        return f"{self.name} {self.surname}"

