from django.db import models

# Create your models here.


class Author(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True)
    name = models.CharField(max_length=255)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Article(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True)
    title = models.CharField(max_length=120)
    description = models.TextField(max_length=3000)
    body = models.TextField(max_length=5000)
    author = models.ForeignKey('Author', related_name='articles', on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.title
