from django.db import models
from django.db.models.fields.related import ForeignKey
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=24)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=48, null=True)
    price = models.IntegerField(null=True)
    description = models.TextField(null=True, blank=True)
    date_posted = models.DateTimeField(default=timezone.now, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts')

    def __str__(self):
        return f'ID:{self.id} Title: {self.title} Price:$ {self.price} Description: {self.description} Date: {self.date_posted} Category: {self.category}'




