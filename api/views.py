from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import status, viewsets
from rest_framework import permissions
from api.serializers import UserSerializer, GroupSerializer
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from django.http import HttpResponse
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout


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
    # login(request, request.user)
    return Response({
        'user': str(request.user),
        'message': 'User is loggedIn'
    }, status=status.HTTP_200_OK)
   
 
def logout_view(request):
    pass

def register_view(request):
    pass

def profile(request):
    pass

def version(request):
    pass