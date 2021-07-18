from django.db import models
from django.db.models.fields.related import ForeignKey
from django.db import models

class Category(models.Model):
    name        = models.CharField(max_length=64)
    category_id = models.CharField(max_length=24)

    def __str__(self):
        return f'{self.name}'

class Post(models.Model):
    name        = models.CharField(max_length=64)
    post_id     = models.CharField(max_length=24)
    description = models.CharField(max_length=128)
    category    = ForeignKey(Category, related_name='posts', on_delete=models.CASCADE)
