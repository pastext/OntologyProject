from django.db import models

# Create your models here.
class elements(models.Model):
    name = models.CharField(max_length=100)
    id = models.IntegerField(primary_key=True)

    def __str__(self):
        return self.name
    
class classes(models.Model):
    name = models.CharField(max_length=100)
    id = models.IntegerField(primary_key=True)

    def __str__(self):
        return self.name