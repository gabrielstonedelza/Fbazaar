from .models import Ordered
from .serializers import OrderedSerializer
from django.shortcuts import get_object_or_404
from django.http import Http404
from rest_framework.decorators import api_view, permission_classes
from rest_framework import viewsets, permissions, generics, status
from rest_framework.response import Response
from order.models import Order


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_ordered_items(request,unique_code):
    ordered = Ordered.objects.filter(user=request.user).filter(ordered=True).filter(unique_order_code=unique_code).order_by('-date_ordered')
    serializer = OrderedSerializer(ordered, many=True)
    return (Response(serializer.data)


@api_view(['GET']))
@permission_classes([permissions.AllowAny])
def get_ordered_items_admin(request,unique_code):
    ordered = Ordered.objects.filter(unique_order_code=unique_code).order_by('-date_ordered')
    serializer = OrderedSerializer(ordered, many=True)
    return Response(serializer.data)