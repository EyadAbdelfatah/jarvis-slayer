from rest_framework import serializers
from .models import Review
from user.serializers import UserSerializer
from book.serializers import BookSerializer

class ReviewSerializer(serializers.ModelSerializer):
  likes = serializers.SerializerMethodField()
  user = UserSerializer(read_only=True)
  book = BookSerializer(read_only=True)

  class Meta:
    model = Review
    fields = ["id", "user", "book", "star_rating", "likes", "written_text", "spoiler", "approved", "created_at", "updated_at"]
    read_only_fields = ["id", "user", "book", "created_at", "updated_at"]

  def get_likes(self, obj):
    return obj.liked_by.count()
  
  def create(self, validated_data):
    review = Review.objects.create(
        user=self.context["request"].user,
        **validated_data
    )
    return review