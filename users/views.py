from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import generics, views
from rest_framework import status
from django.contrib.auth import get_user_model
from .models import User
from .serializers import UserSerializer

# User = get_user_model()


class UserListAPI(views.APIView):
    def get(self, request, pk=None): # Add 'pk=None' to the get method
        if pk is not None:
            user = User.objects.get(pk=pk)
            serializer = UserSerializer(user)
            return Response(serializer.data)
        else:
            user = User.objects.all()
            serializer = UserSerializer(user, many=True)
            return Response(serializer.data)

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

