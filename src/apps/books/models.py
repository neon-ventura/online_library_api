from django.db import models

class BooksModel(models.Model):
    name = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    link = models.CharField(max_length=255)
    publication_date = models.DateField(auto_now_add=True)
