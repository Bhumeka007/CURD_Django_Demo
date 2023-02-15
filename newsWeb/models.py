from django.db import models

# Create your models here.
class News(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    image = models.ImageField(upload_to='static_img')
