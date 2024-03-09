from django.db import models

# Create your models here.
class NPC(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField()

    def __str__(self):
        return self.name