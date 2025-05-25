from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class UserView(APIView):
    
    def get(self, req):
        return Response({"Message": "Here are the all users"}, status.HTTP_200_OK)