from django.db import models

# Create your models here.


class Oringal(models.Model):
    image = models.FileField(upload_to='uploads/')

class Fliter(models.Model):
    image_fliter = models.FileField(upload_to='uploads/')
    