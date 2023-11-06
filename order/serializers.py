from rest_framework import serializers
from .models import Order,ClearedPickUps, ItemsPickedUp,ItemsDroppedOff,QualifiedForBonuses,AssignDriverToOrder,DriversCurrentLocation,ItemsInTransit,PendingOrders,ProcessingOrders


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['id','user','items','payment_method','drop_off_location_lat','drop_off_location_lng','date_order_created','order_status','delivery_method','delivered','ordered','date_ordered','unique_order_code','get_item_details','order_total_price']
        read_only_fields = ['user']


class PendingOrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = PendingOrders
        fields = ['id', 'user_with_order', 'order', 'user', 'date_created', 'order_status',
                  'get_ordered_username', 'get_order_code','pass_pending','get_items']
        read_only_fields = ['user','order']

class ProcessingOrdersSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProcessingOrders
        fields = ['id', 'user_with_order', 'order', 'user', 'date_created', 'order_status',
                  'get_ordered_username', 'get_order_code','pass_processing']
        read_only_fields = ['user','order']

class ItemsInTransitSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemsInTransit
        fields = ['id','user_with_order','order','driver','date_created','order_status','get_username','get_ordered_username','get_order_code','pass_in_transit']
        read_only_fields = ['driver','order']

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
        fields = ['id','order','user','date_created','get_order_code','order_status','get_ordered_username','user_with_order']
        read_only_fields = ['user','order']