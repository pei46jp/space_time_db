from django.db import models
from django.db.models.fields import CharField
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=255)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Bar(models.Model):
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    budget = models.IntegerField(null=True)
    recommend_menu = CharField(max_length=255, null=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('barmap:detail', kwargs={'pk': self.pk})