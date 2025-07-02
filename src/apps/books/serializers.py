from rest_framework import serializers
from apps.books.models import BooksModel

class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = BooksModel
        fields = ['id', 'name', 'author', 'link', 'publication_date']
