from .models import OrderItem
from .serializers import OrderItemSerializer
from django.shortcuts import get_object_or_404
from django.http import Http404
from rest_framework.decorators import api_view, permission_classes
from rest_framework import viewsets, permissions, generics, status
from rest_framework.response import Response
from store_api.models import StoreItem
from order.models import Order,PendingOrders
from order.serializers import OrderSerializer
from ordered.models import Ordered



# new add to cart
@api_view(['GET','POST'])
@permission_classes([permissions.IsAuthenticated])
def item_to_cart(request,id):
    item = get_object_or_404(StoreItem, id=id)
    serializer = OrderItemSerializer(data=request.data)

    if serializer.is_valid():
        # checking if order item is already in cart
        if not OrderItem.objects.filter(item=item).filter(user=request.user).filter(ordered=False).exists():
            serializer.save(user=request.user,item=item)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            order_item = get_object_or_404(OrderItem, item=item)
            if order_item:
                order_item.quantity += 1
                order_item.save()
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# new checkout
@api_view(['GET','POST'])
@permission_classes([permissions.IsAuthenticated])
def item_check_out(request,pm,dm,drop_loc_lat,drop_off_lng,unique_code,total_price):
    items = OrderItem.objects.filter(user=request.user).filter(ordered=False)
    serializer = OrderSerializer(data=request.data)

    if serializer.is_valid():
        ordering_user = Order.objects.create(user=request.user,ordered=True,payment_method=pm,drop_off_location_lat=drop_loc_lat,drop_off_location_lng=drop_off_lng,order_status="Pending",unique_order_code=unique_code,delivery_method=dm,order_total_price=total_price)
        PendingOrders.objects.create(user_with_order=request.user,order=ordering_user,order_status="Pending")
        for i in items:
            Ordered.objects.create(user=request.user,item=i.item,ordered=True,unique_order_code=unique_code)
            i.ordered = True
            i.save()
            ordering_user.items.add(i)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# get my ordered items
@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_my_ordered_items(request):
    ordered_items = Order.objects.filter(user=request.user).filter(ordered=True).order_by('-date_ordered')
    serializer = OrderSerializer(ordered_items, many=True)
    return Response(serializer.data)

# @api_view(['GET','POST'])
# @permission_classes([permissions.IsAuthenticated])
# def add_item_to_cart(request,id):
#     item = get_object_or_404(StoreItem, id=id)
#     de_user = get_object_or_404(Order,user=request.user)
#     serializer = OrderSerializer(data=request.data)
#     # order_item = get_object_or_404(OrderItem, item=item)
#     if serializer.is_valid():
#         # checking if order item is already in cart
#         if not OrderItem.objects.filter(item=item).filter(user=request.user).filter(ordered=False).exists():
#             OrderItem.objects.create(item=item,user=request.user,ordered=False)
#         else:
#             order_item = get_object_or_404(OrderItem, item=item)
#             if order_item:
#                 order_item.quantity += 1
#                 order_item.save()
#         if Order.objects.filter(user=request.user).filter(ordered=False).exists() and not de_user.items.filter(item__id=item.id).exists():
#         # if not de_user.items.filter(item__id=item.id).exists():
#             order_item = get_object_or_404(OrderItem, item=item)
#             de_user.items.add(order_item)
#             # serializer.save(user=de_user)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT'])
@permission_classes([permissions.IsAuthenticated])
def increase_item_quantity(request,id):
    cart_item = get_object_or_404(OrderItem, id=id)
    serializer = OrderItemSerializer(data=request.data)
    if serializer.is_valid():
        cart_item.quantity += 1
        cart_item.save()
        # serializer.save(user=request.user, food=food)
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT'])
@permission_classes([permissions.IsAuthenticated])
def decrease_item_quantity(request,id):
    cart_item = get_object_or_404(OrderItem, id=id)
    serializer = OrderItemSerializer(data=request.data)
    if serializer.is_valid():
        cart_item.quantity -= 1
        cart_item.save()
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


@api_view(['GET', 'DELETE'])
@permission_classes([permissions.IsAuthenticated])
def remove_item_from_cart(request, id):
    try:
        item = get_object_or_404(OrderItem, id=id)
        item.delete()
    except OrderItem.DoesNotExist:
        return Http404
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def clear_order_items(request):
    cart_items = OrderItem.objects.filter(user=request.user).filter(ordered=False).order_by('-date_ordered')
    for i in cart_items:
        i.delete()
    serializer = OrderItemSerializer(cart_items, many=True)
    return Response(serializer.data)