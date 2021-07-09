import api
from codecs import register
from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import generics, serializers, status, viewsets
from rest_framework import permissions
from rest_framework.utils.serializer_helpers import JSONBoundField
from api.serializers import UserSerializer, GroupSerializer
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from django.http import HttpResponse, request
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout
from rest_framework.parsers import JSONParser
from .serializers import RegistrationSerializer



# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]



@api_view(['POST'])
def login_view(request):
    user = str(request.user)
    logged_user = User.objects.get(username=user)
    logged_user.is_active = True
    logged_user.save()
    return Response({
        'username': logged_user.get_username(),
        'loggedIn': logged_user.is_active
    }, status=status.HTTP_200_OK)
   
@api_view(['POST'])
@permission_classes((IsAuthenticated,))
def logout_view(request):
    user = str(request.user)
    logged_user = User.objects.get(username=user)
    logged_user.is_active = False
    logged_user.save()
    return Response({
        'message': "User is logged out"
    }, status=status.HTTP_200_OK)


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes(AllowAny,)
    serializer_class = RegistrationSerializer


    def post(self, request, format=None):
        if request.data == {}:
            return Response({
                'message': "Send request Body"
            }, status=status.HTTP_204_NO_CONTENT) 

        register_serializer = RegistrationSerializer(data=request.data)
        if register_serializer.is_valid():
            register_serializer.is_active = False
            register_serializer.save()
            return Response(
                {
                    'data': register_serializer.data,
                    'message': "You are succesfully registered" 
                },
                status=status.HTTP_201_CREATED
            )
        return Response(register_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def profile(request):
    user = str(request.user)
    logged_user = User.objects.get(username=user)
    if logged_user.is_active:
        return Response({
            'username': logged_user.get_username(),
            'full name': logged_user.get_full_name(),
            'email': logged_user.email,
            'loggedIn': True
        }, status=status.HTTP_200_OK)
    else:
        return Response({
            'message': "User is unauthoriezed to access the information. Please login first"
        }, status=status.HTTP_401_UNAUTHORIZED)
def version(request):
    pass