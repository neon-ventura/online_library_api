from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


books_list = [
  {
    "id": 1,
    "name": "A Jornada do Dev",
    "author": "Lucas Andrade",
    "created_at": "2025-05-01T10:23:45Z"
  },
  {
    "id": 2,
    "name": "Python para Todos",
    "author": "Marina Souza",
    "created_at": "2025-05-02T14:15:30Z"
  },
  {
    "id": 3,
    "name": "O Código Limpo",
    "author": "Carlos Silva",
    "created_at": "2025-05-03T08:40:12Z"
  },
  {
    "id": 4,
    "name": "Django na Prática",
    "author": "Fernanda Ribeiro",
    "created_at": "2025-05-04T11:00:00Z"
  },
  {
    "id": 5,
    "name": "RESTful APIs do Zero",
    "author": "João Mendes",
    "created_at": "2025-05-05T09:12:59Z"
  }
]


class Books (APIView):
    def get(self, req):
        print(f"Get is OK: {status.HTTP_200_OK}")
        return Response({"books": books_list}, status.HTTP_200_OK)
