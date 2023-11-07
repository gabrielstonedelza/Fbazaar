from rest_framework import serializers
from .models import Ordered

class OrderedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ordered
        fields = ['id','user','item','ordered','date_ordered','unique_order_code','get_username','get_item_name','get_item_size','get_item_pic','get_item_price']