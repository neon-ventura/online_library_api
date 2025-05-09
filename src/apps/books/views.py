from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from datetime import datetime, timezone
from .models import Book
from .serializers import BookSerializer


class Books (APIView):
    def get(self, req):
        
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response({"books": serializer.data}, status.HTTP_200_OK)
    
    def post(self, req):
        name = req.data.get('name')
        author = req.data.get('author')
        link = req.data.get('link')

        if not name or not author:
            return Response({"Error: ": "Name and author is required"}, status.HTTP_400_BAD_REQUEST)

        new_book = Book.objects.create(
          name=name,
          author=author,
          link=link,
          created_at=datetime.now(timezone.utc)
        )
        
        serializer = BookSerializer(new_book)

        return Response({"book_created": serializer}, status.HTTP_201_CREATED)

