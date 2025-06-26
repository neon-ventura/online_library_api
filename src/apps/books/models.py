from django.db import models
from apps.users.models import User

class Book(models.Model):
    name = models.CharField(max_length=225)
    author = models.CharField(max_length=255)
    link = models.URLField()
    created_at = models.DateField(auto_now_add=True)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.name