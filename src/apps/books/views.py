from rest_framework import views
from rest_framework import status
from rest_framework.response import Response
from apps.books.models import BooksModel
from apps.books.serializers import BooksSerializer


class BooksView(views.APIView):
    def get(self, request, pk=None):
        
        if pk:
            try:
                book = BooksModel.objects.get(pk=pk)
                serializer = BooksSerializer(book)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except BooksModel.DoesNotExist:
                return Response({'Error': 'Book not found'}, status=status.HTTP_404_NOT_FOUND)
        
        books = BooksModel.objects.all()
        serializer = BooksSerializer(books, many=True)
        
        return Response({"Books": serializer.data}, status.HTTP_200_OK)
    
    
    def post (self, request):
        
        name = request.data.get('name')
        author = request.data.get('author')
        link = request.data.get('link')
        
        if not (name and author and link):
            return Response({'Error: All fields are mandatory'}, status.HTTP_400_BAD_REQUEST)
        
        new_book = BooksModel(name=name, author=author, link=link)
        new_book.save()
        
        return Response({'message': 'You book was created successfully!'}, status.HTTP_201_CREATED)
    
    def delete(self, request, pk):
        try:
            book = BooksModel.objects.get(pk=pk)
            book.delete()
            return Response({'message': 'Book deleted successfully'}, status.HTTP_204_NO_CONTENT)
        except BooksModel.DoesNotExist:
            return Response({'Error': 'Book not found'}, status.HTTP_404_NOT_FOUND)
    
    def put(self, request, pk):
        
        try:
            book = BooksModel.objects.get(pk=pk)
        except BooksModel.DoesNotExist:
            return Response({'Error': 'Book not found'}, status.HTTP_404_NOT_FOUND)
        
        name = request.data.get('name')
        author = request.data.get('author')
        link = request.data.get('link')
        
        if not (name and author and link):
            return Response({'error': 'All fields are mandatory'}, status=status.HTTP_400_BAD_REQUEST)
        
        book.name = name
        book.author = author
        book.link = link
        book.save()
        return Response({'message': 'Book updated successfully!'}, status=status.HTTP_200_OK)
