from rest_framework import serializers
from .models import Cart


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ['id','user','item','price','date_added','get_item_name','get_item_price','get_item_pic','quantity']
        read_only_fields = ['user']