from django.shortcuts import render,get_object_or_404
from .models import RegisterStore
from .serializers import RegisterStoreSerializer
from django.http import Http404
from rest_framework.decorators import api_view, permission_classes
from rest_framework import viewsets, permissions, generics, status
from rest_framework.response import Response


@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def register_store(request):
    serializer = RegisterStoreSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','PUT'])
@permission_classes([permissions.IsAuthenticated])
def update_store(request,id):
    my_store = get_object_or_404(RegisterStore,id=id)
    serializer = RegisterStoreSerializer(my_store,data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_my_store(request):
    my_store = RegisterStore.objects.filter(user=request.user).order_by('-date_created')
    serializer = RegisterStoreSerializer(my_store, many=True)
    return Response(serializer.data)

