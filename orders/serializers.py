from rest_framework import serializers
from .models import OrderItem

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['id','item','user','quantity','ordered','date_ordered','get_item_total_price','get_item_name','get_username','get_item_pic','get_item_size','get_item_price']
        read_only_fields = ['user','item']
