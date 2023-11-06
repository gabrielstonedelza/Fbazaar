from rest_framework import serializers
from .models import Order,ClearedPickUps, ItemsPickedUp,ItemsDroppedOff,QualifiedForBonuses,AssignDriverToOrder,DriversCurrentLocation,ItemsInTransit


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id','user','items','payment_method','drop_off_location_lat','drop_off_location_lng','date_order_created','order_status','delivery_method','delivered','ordered','date_ordered','unique_order_code','get_item_details']
        read_only_fields = ['user']


class ItemsInTransitSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemsInTransit
        fields = ['id','order','driver','date_created']
        read_only_fields = ['driver']
class DriversCurrentLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = DriversCurrentLocation
        fields = ['id','order','driver','user','drivers_lat','drivers_lng','date_created','get_drivers_name','get_order_user']
        read_only_fields = ['driver','order']

class AssignDriverToOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssignDriverToOrder
        fields = ['id','order','driver','date_created','get_item_code','get_ordered_username',]
        read_only_fields = ['order']

class ClearedPickUpsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClearedPickUps
        fields = ['id',]

class ItemsPickedUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemsPickedUp
        fields = ['id','order','user','date_created','get_username']
        read_only_fields = ['user']


class ItemsDroppedOffSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemsDroppedOff
        fields = ['id','order','user','date_created','get_item_name','get_item_size','get_item_pic','get_ordered_username','get_order_quantity','get_order_status','get_item_price']
        read_only_fields = ['user']