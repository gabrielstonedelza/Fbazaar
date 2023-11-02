from .models import OrderItem
from .serializers import OrderItemSerializer
from django.shortcuts import get_object_or_404
from django.http import Http404
from rest_framework.decorators import api_view, permission_classes
from rest_framework import viewsets, permissions, generics, status
from rest_framework.response import Response
from store_api.models import StoreItem
from order.models import Order
from order.serializers import OrderSerializer


@api_view(['GET','POST'])
@permission_classes([permissions.IsAuthenticated])
def add_item_to_cart(request,id):
    item = get_object_or_404(StoreItem, id=id)
    de_user = get_object_or_404(Order,user=request.user)
    serializer = OrderSerializer(data=request.data)
    # order_item = get_object_or_404(OrderItem, item=item)
    if serializer.is_valid():
        # checking if order item is already in cart
        if not OrderItem.objects.filter(item=item).filter(user=request.user).filter(ordered=False).exists():
            OrderItem.objects.create(item=item,user=request.user,ordered=False)
        else:
            order_item = get_object_or_404(OrderItem, item=item)
            if order_item:
                order_item.quantity += 1
                order_item.save()
        if Order.objects.filter(user=request.user).filter(ordered=False).exists() and not de_user.items.filter(item__id=item.id).exists():
        # if not de_user.items.filter(item__id=item.id).exists():
            order_item = get_object_or_404(OrderItem, item=item)
            de_user.items.add(order_item)
            # serializer.save(user=de_user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT'])
@permission_classes([permissions.IsAuthenticated])
def increase_item_quantity(request,id,item_id):
    item = get_object_or_404(StoreItem, id=item_id)
    cart_item = get_object_or_404(OrderItem, id=id)
    serializer = OrderItemSerializer(data=request.data)
    if serializer.is_valid():
        cart_item.quantity += 1
        cart_item.save(user=request.user,item=item)
        # serializer.save(user=request.user, food=food)
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT'])
@permission_classes([permissions.IsAuthenticated])
def decrease_item_quantity(request,id,item_id):
    item = get_object_or_404(StoreItem, id=item_id)
    cart_item = get_object_or_404(OrderItem, id=id)
    serializer = OrderItemSerializer(data=request.data)
    if serializer.is_valid():
        cart_item.quantity -= 1
        cart_item.save(user=request.user,item=item)
        # serializer.save(user=request.user, food=food)
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_not_ordered_items(request):
    cart_items = OrderItem.objects.filter(user=request.user).filter(ordered=False).order_by('-date_ordered')
    serializer = OrderItemSerializer(cart_items, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_ordered_items(request):
    ordered_items = OrderItem.objects.filter(user=request.user).filter(ordered=True).order_by('-date_ordered')
    serializer = OrderItemSerializer(ordered_items, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def check_out_order_items(request):
    cart_items = OrderItem.objects.filter(user=request.user).filter(ordered=False).order_by('-date_ordered')
    for i in cart_items:
        i.ordered = True
        i.save()
    serializer = OrderItemSerializer(cart_items, many=True)
    return Response(serializer.data)

@api_view(['GET','POST'])
@permission_classes([permissions.IsAuthenticated])
def remove_item_from_cart(request,id,order_item_id):
    item = get_object_or_404(StoreItem, id=id)
    de_user = get_object_or_404(Order,user=request.user)
    serializer = OrderSerializer(data=request.data)
    # order_item = get_object_or_404(OrderItem, item=item)
    if serializer.is_valid():
        # checking if order item is already in cart
        if Order.objects.filter(user=request.user).filter(ordered=False).exists() and de_user.items.filter(item__id=item.id).exists():
            order_item = get_object_or_404(OrderItem, item=item)
            de_user.items.remove(order_item)
            order_item.delete()
        if OrderItem.objects.filter(item=item).filter(user=request.user).filter(ordered=False).exists():
            order_item = get_object_or_404(OrderItem, id=order_item_id)
            order_item.delete()
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def clear_order_items(request):
    cart_items = OrderItem.objects.filter(user=request.user).filter(ordered=False).order_by('-date_ordered')
    for i in cart_items:
        i.delete()
    serializer = OrderItemSerializer(cart_items, many=True)
    return Response(serializer.data)