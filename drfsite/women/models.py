from django.db import models
from django.contrib.auth.models import User


class Women(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Пользователи')

    class Meta:
        verbose_name_plural = 'Women'
        verbose_name = 'Woman'

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=50, db_index=True)

    class Meta:
        verbose_name_plural = 'Categories'
        verbose_name = 'Category'

    def __str__(self):
        return self.name




