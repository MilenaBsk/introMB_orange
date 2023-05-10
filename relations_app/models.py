from django.db import models

# Create your models here.
# ONE to ONE
class Country(models.Model):
    name = models.CharField(max_length=64)
    capital = models.OneToOneField('Capital', on_delete=models.CASCADE)

class Capital(models.Model):
    name = models.CharField(max_length=64)

# ONE to MANY
class Language(models.Model):
    name = models.CharField(max_length=64)

class Framework(models.Model):
    name = models.CharField(max_length=64)
    language = models.ForeignKey('Language', on_delete=models.CASCADE)

class Actor(models.Model):
    name = models.CharField(max_length=64)
class Movie(models.Model):
    title = models.CharField(max_length=128)
    actors = models.ManyToManyField('Actor')