from django.shortcuts import render,get_object_or_404

from .models import StoreItem,AddToPriceChanged,ItemRatings,ItemRemarks
from .serializers import StoreItemSerializer,ItemRatingsSerializer,AddToPriceChangedSerializer,ItemRemarksSerializer,NotifyAboutItemVerifiedSerializer,NotifyAboutItemRejectedSerializer

from django.http import Http404
from rest_framework.decorators import api_view, permission_classes
from rest_framework import viewsets, permissions, generics, status
from rest_framework.response import Response
from datetime import datetime, date, time
from rest_framework import filters


# verify items
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def verify_item(request,id):
    item = get_object_or_404(StoreItem,id=id)
    serializer = NotifyAboutItemVerifiedSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(item=item)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def reject_item(request,id):
    item = get_object_or_404(StoreItem, id=id)
    serializer = NotifyAboutItemRejectedSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(item=item)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
# add and update items
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def add_item(request):
    serializer = StoreItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_all_my_items(request):
    items = StoreItem.objects.filter(user=request.user).order_by('-date_created')
    serializer = StoreItemSerializer(items, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_all_items(request):
    items = StoreItem.objects.all().order_by('-date_created')
    serializer = StoreItemSerializer(items, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_all_verified_items(request):
    items = StoreItem.objects.filter(item_verified=True).order_by('-date_created')
    serializer = StoreItemSerializer(items, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_all_unverified_items(request):
    items = StoreItem.objects.filter(item_verified=False).filter(item_rejected=False).order_by('-date_created')
    serializer = StoreItemSerializer(items, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_item_detail(request,id):
    item = get_object_or_404(StoreItem,id=id)
    serializer = StoreItemSerializer(item, many=False)
    return Response(serializer.data)

@api_view(['GET', 'PUT'])
@permission_classes([permissions.IsAuthenticated])
def update_item(request, id):
    item = get_object_or_404(StoreItem, id=id)
    serializer = StoreItemSerializer(item, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'DELETE'])
@permission_classes([permissions.IsAuthenticated])
def delete_item(request, id):
    try:
        item = get_object_or_404(StoreItem, id=id)
        item.delete()
    except StoreItem.DoesNotExist:
        return Http404
    return Response(status=status.HTTP_204_NO_CONTENT)


# add to price change starts here
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def add_to_price_change(request):
    serializer = AddToPriceChangedSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# remarks
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def add_remarks(request,id):
    item = get_object_or_404(StoreItem, id=id)
    serializer = ItemRemarksSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user,item=item)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_all_remarks(request):
    remarks = ItemRemarks.objects.all().order_by('-date_added')
    serializer = ItemRemarksSerializer(remarks, many=True)
    return Response(serializer.data)

@api_view(['GET', 'DELETE'])
@permission_classes([permissions.IsAuthenticated])
def delete_remark(request, id):
    try:
        item = get_object_or_404(ItemRemarks, id=id)
        item.delete()
    except ItemRemarks.DoesNotExist:
        return Http404
    return Response(status=status.HTTP_204_NO_CONTENT)

# ratings
@api_view(['POST'])
@permission_classes([permissions.IsAuthenticated])
def add_rating(request):
    serializer = ItemRatingsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_all_ratings(request):
    remarks = ItemRatings.objects.all().order_by('-date_rated')
    serializer = ItemRatingsSerializer(remarks, many=True)
    return Response(serializer.data)

# get item ratings and remarks

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_all_item_ratings(request,id):
    item = get_object_or_404(StoreItem, id=id)
    ratings = ItemRatings.objects.filter(item=item).order_by('-date_rated')
    serializer = ItemRatingsSerializer(ratings, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_all_item_remarks(request,id):
    item = get_object_or_404(StoreItem, id=id)
    remarks = ItemRemarks.objects.filter(item=item).order_by('-date_added')
    serializer = ItemRemarksSerializer(remarks, many=True)
    return Response(serializer.data)

class SearchForItem(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    queryset = StoreItem.objects.filter(item_verified=True).order_by("-date_created")
    serializer_class = StoreItemSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'category']

    # get exclusive, promotion and other items

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_exclusive_items(request):
    items = StoreItem.objects.filter(exclusive=True).filter(item_verified=True).order_by('-date_created')
    serializer = StoreItemSerializer(items, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_promotion_items(request):
    items = StoreItem.objects.filter(promotion=True).filter(item_verified=True).order_by('-date_created')
    serializer = StoreItemSerializer(items, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_other_items(request):
    items = StoreItem.objects.filter(promotion=False).filter(item_verified=True).filter(exclusive=False).order_by('-date_created')
    serializer = StoreItemSerializer(items, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_drinks(request):
    items = StoreItem.objects.filter(category="Drinks").filter(item_verified=True).order_by('-date_created')
    serializer = StoreItemSerializer(items, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([permissions.IsAuthenticated])
def get_water(request):
    items = StoreItem.objects.filter(category="Water").filter(item_verified=True).order_by('-date_created')
    serializer = StoreItemSerializer(items, many=True)
    return Response(serializer.data)

