from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from datetime import datetime, timezone
from .models import Book
from .serializers import BookSerializer


class Books (APIView):
    def get(self, req):
        name = req.query_params.get('name', None)
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        
        if name:
            books = Book.objects.filter(name__icontains=name)
            serielizer = BookSerializer(books, many=True)
            return Response({"books": serielizer.data}, status.HTTP_200_OK)
        
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

        return Response({"book_created": serializer.data}, status.HTTP_201_CREATED)
    
    def put(self, req, pk):
        
        try:
            book = Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            return Response({"Error": "Book not found"}, status.HTTP_404_NOT_FOUND)
        
        name = req.data.get('name')
        author = req.data.get('author')
        link = req.data.get('link')
        
        if not name or not author or not link:
            return Response({"Error": "Parameters is required"}, status.HTTP_400_BAD_REQUEST)
        book.name = name
        book.author = author
        book.link = link
        book.save()
        return Response({"Book updated!", status.HTTP_200_OK})
    
    def delete(self, req, pk):
        try:
            book = Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            return Response({"Book not found!"}, status.HTTP_404_NOT_FOUND)
        
        serializer = BookSerializer(book)
        
        book.delete()
        return Response({"Book deleted!": serializer.data}, status.HTTP_200_OK)
        
        
        

