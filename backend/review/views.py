from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .serializers import ReviewSerializer
from .models import Review

# Create your views here.

class ReviewViewSet(viewsets.ModelViewSet):
  queryset = Review.objects.all()
  serializer_class = ReviewSerializer
  permission_classes = [IsAuthenticated]

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
  
  @action(detail=True, methods=["patch"], permission_classes=[IsAdminUser])
  def approve(self, request, pk=None):
    review = self.get_object()

    review.approved = True
    review.save()

    return Response({
      "message": "Review approved"
    })