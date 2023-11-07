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
def get_ordered_items(request):
    orders_by_unique_code = []
    ordered_items = Order.objects.filter(user=request.user).filter(ordered=True).order_by('-date_ordered')
    ordered = Ordered.objects.filter(user=request.user).filter(ordered=True).order_by('-date_ordered')
    for i in ordered:
        if i.unique_order_code in ordered_items:
            orders_by_unique_code.append(i)
    serializer = OrderedSerializer(orders_by_unique_code, many=True)
    return Response(serializer.data)