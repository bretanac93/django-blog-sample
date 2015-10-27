from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Blog(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=160)
    owner = models.ForeignKey(User)
    creation_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Entry(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    creator = models.ForeignKey(User)
    creation_date = models.DateTimeField(auto_now=True)
    blog = models.ForeignKey(Blog)

    def __str__(self):
        return self.title