from django.db import models


class Author(models.Model):
    full_name = models.CharField(max_length=255)
    birth_date = models.CharField(max_length=10)
    country = models.CharField(max_length=155)

    def __str__(self):
        return self.full_name

class Book(models.Model):
    title = models.CharField(max_length=255)
    published_year = models.CharField()
    pages = models.SmallIntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True, related_name='books')