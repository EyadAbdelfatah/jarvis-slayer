from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import ReviewSerializer
from .models import Review
from rest_framework.permissions import IsAuthenticated
from core.permissions import (
    IsAdmin,
    IsAdminOrOwner,
    IsStudentAndOwnsObject,
)

class ReviewViewSet(viewsets.ModelViewSet):
  queryset = Review.objects.all()
  serializer_class = ReviewSerializer
  
  def get_permissions(self):
    if self.action in ["approve"]:
      permission_classes = [IsAdmin]
    elif self.action in ["destroy"]:
      permission_classes = [IsAdminOrOwner]
    elif self.action in ["update", "partial_update"]:
      permission_classes = [IsStudentAndOwnsObject]
    else:
      permission_classes = [IsAuthenticated]
    return [p() for p in permission_classes]

  @action(detail=True, methods=["post"])
  def like(self, request, pk=None):
    review = self.get_object()

    review.liked_by.add(request.user)

    return Response({
      "message": "Review liked"
    })
  
  @action(detail=True, methods=["post"])
  def unlike(self, request, pk=None):
    review = self.get_object()

    review.liked_by.remove(request.user)

    return Response({
      "message": "Review unliked"
    })
  
  @action(detail=True, methods=["patch"])
  def approve(self, request, pk=None):
    review = self.get_object()

    review.approved = True
    review.save()

    return Response({
      "message": "Review approved"
    })