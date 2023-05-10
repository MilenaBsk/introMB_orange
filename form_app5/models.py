from django.db import models


# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=100)

    def str(self):
        return self.name


# One-to-one (O2O)
class Country(models.Model):
    name = models.CharField(max_length=100)
    capital = models.OneToOneField('Capital', on_delete=models.CASCADE)

class Capital(models.Model):
    name = models.CharField(max_length=100)


# One-to-many (O2M)
class Language(models.Model):
    name = models.CharField(max_length=100)
    # framework_set =  # automatycznie dorobiony przez django menadżer powiązany

class Framework(models.Model):
    name = models.CharField(max_length=100)
    language = models.ForeignKey('Language', on_delete=models.CASCADE)
    # language_id = ...  # automatycznie dorobione przez django pole

class Actor(models.Model):
    name = models.CharField(max_length=100)


class Movie(models.Model):
    title = models.CharField(max_length=128)
    actors = models.ManyToManyField('Actor')