from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=64, null=False, blank=False)

    def __str__(self):
        return self.name


class Photo(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    description = models.CharField(max_length=64, null=True, blank=True)
    image = models.ImageField(upload_to='photos', null=False, blank=False)

    def __str__(self):
        return self.description
