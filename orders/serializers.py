from rest_framework import serializers
from .models import OrderItem, ClearedPickUps, ItemsPickedUp,ItemsDroppedOff,QualifiedForBonuses


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['id','item','user','quantity','category','size','price','payment_method','drop_off_location_lat','drop_off_location_lng','date_order_created','order_status','ordered','get_item_name','get_username','get_item_pic']
        read_only_fields = ['user','item']


class ClearedPickUpsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClearedPickUps
        fields = "__all__"

class ItemsPickedUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemsPickedUp
        fields = "__all__"


class ItemsDroppedOffSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemsDroppedOff
        fields = "__all__"

class QualifiedForBonusesSerializer(serializers.ModelSerializer):
    class Meta:
        model = QualifiedForBonuses
        fields = "__all__"