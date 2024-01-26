from django.db import models

# Create your models here.
class Service(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15, blank=True, null=True)
    message = models.TextField()

class Vacancy(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    
class MyModel(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name