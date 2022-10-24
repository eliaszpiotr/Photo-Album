from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=64, null=False, blank=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Photo(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    description = models.CharField(max_length=64, null=True, blank=True)
    image = models.ImageField(null=False, blank=False)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = 'Photo'
        verbose_name_plural = 'Photos'