from django.db import models

# Create your models here.

class TelefonbuchEintrag(models.Model):

    name = models.CharField(max_length=30)
    nummer = models.CharField(max_length=30)

    def __str__(self):
        return self.name