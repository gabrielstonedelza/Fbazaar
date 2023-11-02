from django.shortcuts import get_object_or_404
from .models import Order, ClearedPickUps, ItemsPickedUp,ItemsDroppedOff,AssignDriverToOrder,DriversCurrentLocation,ItemsInTransit
from .serializers import OrderSerializer,ClearedPickUpsSerializer,ItemsPickedUpSerializer,ItemsDroppedOffSerializer,AssignDriverToOrderSerializer,DriversCurrentLocationSerializer,ItemsInTransitSerializer
from django.http import Http404
from rest_framework.decorators import api_view, permission_classes
from rest_framework import viewsets, permissions, generics, status
from rest_framework.response import Response
from datetime import datetime, date, time
from django.core.mail import EmailMessage
from .sendemail import send_my_mail
from store_api.models import StoreItem
from orders.models import OrderItem
from .serializers import OrderSerializer


# @api_view(['GET', 'PUT'])
# @permission_classes([permissions.IsAuthenticated])
# def check_out(request):
#     serializer = OrderSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save(user=request.user)
#         return Response(serializer.data)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_cart_items(request):
    cart_items = Order.objects.filter(user=request.user).filter(ordered=False).order_by('-date_ordered')
    serializer = OrderSerializer(cart_items, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_ordered_items(request):
    cart_items = Order.objects.filter(user=request.user).filter(ordered=True).order_by('-date_ordered')
    serializer = OrderSerializer(cart_items, many=True)
    return Response(serializer.data)

@api_view(['GET','PUT'])
@permission_classes([permissions.IsAuthenticated])
def check_out_items(request,id):
    my_order = get_object_or_404(Order,id=id)
    order_items = OrderItem.objects.filter(user=request.user).filter(ordered=False)
    for item in order_items:
        item.ordered = True
        item.save()
    cart_items = Order.objects.filter(user=request.user).filter(ordered=False).order_by('-date_ordered')
    for i in cart_items:
        i.ordered = True
        i.save()
    serializer = OrderSerializer(my_order,data=request.data)
    if serializer.is_valid():
        cart_item.quantity += 1
        cart_item.save()
        serializer.save(user=request.user)
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_my_delivered_order(request):
    delivered_orders = ItemsDroppedOff.objects.filter(user=request.user).order_by('-date_created')
    serializer = ItemsDroppedOffSerializer(delivered_orders, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_my_orders(request):
    orders = Order.objects.filter(user=request.user).order_by('-date_ordered')
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data)

@api_view(['GET', 'PUT'])
@permission_classes([permissions.IsAuthenticated])
def update_order(request, id):
    order = get_object_or_404(OrderItem, id=id)
    serializer = OrderSerializer(order, data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'DELETE'])
@permission_classes([permissions.IsAuthenticated])
def delete_order(request, id):
    try:
        order = get_object_or_404(Order, id=id)
        order.delete()
    except OrderItem.DoesNotExist:
        return Http404
    return Response(status=status.HTTP_204_NO_CONTENT)


# cleared for pickup
@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def add_to_cleared(request):
    serializer = ClearedPickUpsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_cleared_for_pickup(request):
    orders = Order.objects.filter(order_pick_up_status="Cleared for pickup").order_by('-date_ordered')
    serializer = OrderSerializer(orders, many=True)
    return (Response(serializer.data)

@api_view(['GET']))
@permission_classes([permissions.IsAuthenticated])
def get_orders_picked_up(request):
    orders = Order.objects.filter(order_picked_up_status="Items Picked").order_by('-date_ordered')
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data)

@permission_classes([permissions.IsAuthenticated])
def get_orders_dropped_off(request):
    orders = Order.objects.filter(item_dropped_off=True).order_by('-date_ordered')
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data)


# orders picked up
@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def add_to_picked_up_orders(request):
    serializer = ItemsPickedUpSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# order in transit
@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def add_order_to_in_transit(request):
    serializer = ItemsInTransitSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(driver=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# order dropped off
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def add_dropped_off_orders(request):
    serializer = ItemsDroppedOffSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# get orders(pending,processing,picked up,delivered)
@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_all_pending_orders(request):
    orders = Order.objects.filter(order_status="Pending").order_by('-date_ordered')
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_all_processing_orders(request):
    orders = Order.objects.filter(order_status="Processing").order_by('-date_ordered')
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_all_piked_up_orders(request):
    orders = Order.objects.filter(order_status="Picked Up").order_by('-date_ordered')
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_all_in_transit_orders(request):
    orders = Order.objects.filter(order_status="In Transit").filter(assigned_driver=request.user).order_by('-date_ordered')
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_customers_order_in_transit(request):
    orders = Order.objects.filter(order_status="In Transit").filter(user=request.user).order_by('-date_ordered')
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_all_delivered_orders(request):
    orders = Order.objects.filter(order_status="Delivered").order_by('-date_ordered')
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data)
# send_my_mail(f"Hi from ConnectDjango", settings.EMAIL_HOST_USER, i.email, {"name": i.username},
#                          "email_templates/success.html")


# get users pending,processing,picked up and delivered orders
@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_all_my_pending_orders(request):
    orders = Order.objects.filter(user=request.user).filter(order_status="Pending").order_by('-date_ordered')
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_all_my_processing_orders(request):
    orders = Order.objects.filter(user=request.user).filter(order_status="Processing").order_by('-date_ordered')
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_all_my_picked_up_orders(request):
    orders = Order.objects.filter(user=request.user).filter(order_status="Picked Up").order_by('-date_ordered')
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_all_my_delivered_orders(request):
    orders = Order.objects.filter(user=request.user).filter(order_status="Delivered").order_by('-date_ordered')
    serializer = OrderSerializer(orders, many=True)
    return Response(serializer.data)


# assign a driver to order
@api_view(['GET','POST'])
@permission_classes([permissions.AllowAny])
def assign_driver_to_order(request,id):
    order = get_object_or_404(OrderItem, id=id)
    serializer = AssignDriverToOrderSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(order_item=order)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_all_my_assigned_orders(request):
    orders = AssignDriverToOrder.objects.filter(driver=request.user).order_by('-date_created')
    serializer = AssignDriverToOrderSerializer(orders, many=True)
    return Response(serializer.data)


# driver heading to user's location
@api_view(['POST'])
@permission_classes([permissions.AllowAny])
def driver_to_user_location(request):
    serializer = DriversCurrentLocationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(driver=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_all_my_assigned_orders(request):
    orders = AssignDriverToOrder.objects.filter(driver=request.user).order_by('-date_created')
    serializer = AssignDriverToOrderSerializer(orders, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_all_drivers_assigned_orders(request):
    orders = OrderItem.objects.filter(assigned_driver=request.user).filter(delivered=False).order_by('-date_ordered')
    serializer = OrderItemSerializer(orders, many=True)
    return Response(serializer.data)



@api_view(['GET','POST'])
@permission_classes([permissions.IsAuthenticated])
def add_drivers_current_location(request,id):
    order = get_object_or_404(OrderItem, id=id)
    serializer = DriversCurrentLocationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(driver=request.user,order_item=order)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_drivers_current_location(request,id):
    order = get_object_or_404(OrderItem, id=id)
    current_location = DriversCurrentLocation.objects.filter(user=request.user).filter(order_item=order).order_by('-date_created')[:1]
    serializer = DriversCurrentLocationSerializer(current_location, many=True)
    return Response(serializer.data)
