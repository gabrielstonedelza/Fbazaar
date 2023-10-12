from django.shortcuts import render,get_object_or_404
from .models import Cart
from .serializers import CartSerializer
from django.http import Http404
from rest_framework.decorators import api_view, permission_classes
from rest_framework import viewsets, permissions, generics, status
from rest_framework.response import Response
from store_api.models import StoreItem


# @api_view(['POST'])
# @permission_classes([permissions.IsAuthenticated])
# def add_item_to_cart(request):
#     serializer = CartSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save(user=request.user)
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','POST'])
@permission_classes([permissions.IsAuthenticated])
def add_item_to_cart(request,id):
    item = get_object_or_404(StoreItem, id=id)
    serializer = CartSerializer(data=request.data)
    if serializer.is_valid():
        if not Cart.objects.filter(item=item).filter(user=request.user).exists():
            serializer.save(user=request.user,item=item)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_all_my_cart_items(request):
    items = Cart.objects.filter(user=request.user).order_by('-date_added')
    serializer = CartSerializer(items, many=True)
    return Response(serializer.data)


@api_view(['GET', 'DELETE'])
@permission_classes([permissions.IsAuthenticated])
def delete_item_from_cart(request, id):
    try:
        item = get_object_or_404(Cart, id=id)
        item.delete()
    except Cart.DoesNotExist:
        return Http404
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def clear_cart(request):
    items = Cart.objects.filter(user=request.user)
    for item in items:
        item.delete()
    serializer = CartSerializer(items,many=True)
    return Response(serializer.data)


@api_view(['GET','PUT'])
@permission_classes([permissions.IsAuthenticated])
def increase_item_quantity(request,id):
    cart_item = get_object_or_404(Cart, id=id)
    serializer = CartSerializer(data=request.data)
    if serializer.is_valid():
        cart_item.quantity += 1
        cart_item.save()
        # serializer.save(user=request.user, food=food)
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT'])
@permission_classes([permissions.IsAuthenticated])
def decrease_item_quantity(request,id):
    cart_item = get_object_or_404(Cart, id=id)
    serializer = CartSerializer(data=request.data)
    if serializer.is_valid():
        cart_item.quantity -= 1
        cart_item.save()
        # serializer.save(user=request.user, food=food)
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)