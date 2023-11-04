from django.shortcuts import render,get_object_or_404
from rest_framework.decorators import api_view, permission_classes
from rest_framework import viewsets, permissions, generics, status
from rest_framework.response import Response
from .serializers import UsersSerializer
from .models import User

# Create your views here.
def home(request):
    return render(request,"users/home.html")

@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def get_users(request):
    users = User.objects.all()
    serializer = UsersSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['GET', 'PUT'])
@permission_classes([permissions.IsAuthenticated])
def update_user(request, id):
    user = get_object_or_404(User, id=id)
    serializer = UsersSerializer(user, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def get_all_customers(request):
    customers = User.objects.filter(user_type="Customer")
    serializer = UsersSerializer(customers, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def get_all_drivers(request):
    drivers = User.objects.filter(user_type="Driver")
    serializer = UsersSerializer(drivers, many=True)
    return Response(serializer.data)

@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def get_all_wholesale_managers(request):
    managers = User.objects.filter(user_type="Warehouse Manager")
    serializer = UsersSerializer(managers, many=True)
    return Response(serializer.data)


@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def get_admin(request):
    admin_user = User.objects.filter(user_type="Administrator")
    serializer = UsersSerializer(admin_user, many=True)
    return Response(serializer.data)

# send registration otp
@api_view(['GET'])
@permission_classes([permissions.AllowAny])
def send_otp(request,otp,email,username):
    send_my_mail(f"Hello from FBazaar", settings.EMAIL_HOST_USER, email, {"name": username,"OTP": otp},"email_templates/sendotp.html")
    return Response()