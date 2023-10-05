
from rest_framework import serializers
from .models import  Profile



class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField('get_username')

    class Meta:
        model = Profile
        fields = ['id','user', 'profile_pic', 'get_profile_pic', 'get_phone',
                  'get_email', 'get_username','full_name']
        read_only_fields = ['user']