from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from datetime import datetime, timezone


books_list = [
  {
    "id": 1,
    "name": "As 48 leis do poder",
    "author": "Lucas Andrade",
    "link": "https://masculinistaopressoroficial.wordpress.com/wp-content/uploads/2017/06/as-48-leis-do-poder-robert-greene.pdf",
    "created_at": "2025-05-01T10:23:45Z"
  }
]


class Books (APIView):
    def get(self, req):
        print(f"Get is OK: {status.HTTP_200_OK}")
        return Response({"books": books_list}, status.HTTP_200_OK)
    
    def post(self, req):
        id = req.data.get('id')
        name = req.data.get('name')
        author = req.data.get('author')
        link = req.data.get('link')

        if not name or not author:
            return Response({"Error: ": "Name and author is required"}, status.HTTP_400_BAD_REQUEST)

        current_date = datetime.now(timezone.utc).isoformat()

        new_book = {
            "id": id,
            "name" : name,
            "author": author,
            "link": link,
            "created_at": current_date
        }

        books_list.append(new_book)

        return Response({"book_created": new_book}, status.HTTP_201_CREATED)

