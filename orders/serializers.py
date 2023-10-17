from rest_framework import serializers
from .models import OrderItem, ClearedPickUps, ItemsPickedUp,ItemsDroppedOff,QualifiedForBonuses


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = ['id','cart','user','quantity','category','size','price','payment_method','drop_off_location_lat','drop_off_location_lng','date_order_created','order_status','ordered','get_item_name','get_username','get_item_pic','unique_order_code','delivery_method']
        read_only_fields = ['user','cart']


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