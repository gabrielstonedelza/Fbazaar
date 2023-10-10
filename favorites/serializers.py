from rest_framework import serializers
from .models import Favorites

class FavoritesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Favorites
        fields = ['id','user','item','date_added','get_item_name','get_item_price','get_item_pic']
        read_only_fields = ['user']