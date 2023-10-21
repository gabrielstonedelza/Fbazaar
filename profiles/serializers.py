
from rest_framework import serializers
from .models import  Profile



class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['id','user', 'profile_pic', 'get_profile_pic', 'get_phone',
                  'get_email', 'get_username','get_users_fullname']
        read_only_fields = ['user']