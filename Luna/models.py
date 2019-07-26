from django.db import models


# Create your models here.
class Hosts(models.Model):
    name = models.CharField(max_length=200)
    ip = models.CharField(max_length=11)
    host = models.CharField(max_length=100)
    tags = models.CharField(max_length=50)

    def __str__(self):
        return self.name
