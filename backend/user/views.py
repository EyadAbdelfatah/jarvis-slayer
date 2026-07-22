from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import UserSerializer, RegisterSerializer
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

class RegisterView(APIView):
  permission_classes = []

  def post(self, request):
    serializer = RegisterSerializer(
      data=request.data
    )
    serializer.is_valid(
      raise_exception=True
    )
    user = serializer.save()
    return Response(
      {
        "message": "Account created",
        "email": user.email
      },
      status=status.HTTP_201_CREATED
    )