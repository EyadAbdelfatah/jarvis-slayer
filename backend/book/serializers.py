from rest_framework import serializers
from .models import Book
from django.db.models import Avg

class BookSerializer(serializers.ModelSerializer):
  avg_star_rating = serializers.SerializerMethodField()

  class Meta:
    model = Book
    fields = ["id", "author", "title", "description", "cover", "genres", "archived", "avg_star_rating"]
    read_only_fields = ["id", "author", "title", "avg_star_rating"]

  def get_avg_star_rating(self, obj):
    return obj.reviews.aggregate(
      star_rating_avg = Avg("star_rating")
    )["star_rating_avg"]