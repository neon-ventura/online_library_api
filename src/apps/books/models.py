from django.db import models

class Book(models.Model):
    name = models.CharField(max_length=225)
    author = models.CharField(max_length=255)
    link = models.URLField()
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.name