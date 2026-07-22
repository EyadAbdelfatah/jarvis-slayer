from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import UserSerializer
from .models import CustomUser
from rest_framework.permissions import IsAuthenticated
from core.permissions import (
    IsAdmin,
    IsAdminOrOwner,
)

class UserViewSet(viewsets.ModelViewSet):
  queryset = CustomUser.objects.all()
  serializer_class = UserSerializer
  
  def get_permissions(self):
    if self.action in ["list", "create", "destroy"]:
      permission_classes = [IsAdmin]
    elif self.action in ["retrieve", "update", "partial_update"]:
      permission_classes = [IsAdminOrOwner]
    else:
      permission_classes = [IsAuthenticated]
    return [p() for p in permission_classes]
