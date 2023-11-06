from rest_framework import serializers
from .models import StoreItem,AddToPriceChanged,ItemRatings,ItemRemarks, NotifyAboutItemVerified,NotifyAboutItemRejected


class NotifyAboutItemVerifiedSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotifyAboutItemVerified
        fields = ['id','item','user','date_verified']
        read_only_fields = ['item']
class NotifyAboutItemRejectedSerializer(serializers.ModelSerializer):
    class Meta:
        model = NotifyAboutItemRejected
        fields = ['id','item','user','date_rejected']
        read_only_fields = ['item']


class StoreItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = StoreItem
        fields = ['id','user','company_name','name','category','size','old_price','new_price','retail_price','wholesale_price','picture','description','date_created','quantity_qualify_for_free_delivery','exclusive','promotion','quantity_needed_for_wholesale_price','get_item_pic','volume','item_verified','item_rejected']


class ItemRatingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemRatings
        fields = ['id','item','user','rating','date_rated']
        read_only_fields = ['user']

class AddToPriceChangedSerializer(serializers.ModelSerializer):
    class Meta:
        model = AddToPriceChanged
        fields = "__all__"


class ItemRemarksSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemRemarks
        fields = ['id','item','user','remark','date_added','get_username','rating','get_profile_pic']
        read_only_fields = ['user','item']