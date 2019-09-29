from django.db import models

# Create your models here.

class Products(models.Model):
    name = models.CharField(max_length=200)
    desc = models.TextField()
    image = models.ImageField(upload_to='pics')
    musttry = models.BooleanField(default=False)