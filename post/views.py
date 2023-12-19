from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from asgiref.sync import sync_to_async
from .models import Post
from .serializers import PostSerializer

from django.http import Http404
from rest_framework.decorators import api_view,permission_classes
from rest_framework import  permissions

@sync_to_async
@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def add_post(request):
    serializer = PostSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@sync_to_async
@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def get_all_post(request):
    posts = Post.objects.all()
    serializer = PostSerializer(posts, many=True)
    return Response(serializer.data)