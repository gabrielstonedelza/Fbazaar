from rest_framework import serializers
from .models import RegisterStore

class RegisterStoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegisterStore
        fields = ['id','user','name','location','date_created','get_username']
        read_only_fields = ['user']