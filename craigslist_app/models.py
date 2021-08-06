from django.db import models
from django.db.models.fields.related import ForeignKey
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=24)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=48)
    price = models.IntegerField()
    description = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    category = ForeignKey(Category, related_name="posts", on_delete=models.CASCADE)




