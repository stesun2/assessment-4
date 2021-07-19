from django.db import models
from django.db.models.fields.related import ForeignKey

class Category(models.Model):
    name = models.CharField(max_length=24)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=48)
    price = models.IntegerField()
    description = models.TextField()
    category = ForeignKey(Category, related_name="posts", on_delete=models.CASCADE)




