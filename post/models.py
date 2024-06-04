from django.db import models

# Create your models here.
class productAdd(models.Model):
    title = models.CharField(max_length=20)
    text = models.TextField(max_length=100)
    image = models.ImageField(upload_to='image/')