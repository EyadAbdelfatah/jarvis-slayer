from django.db import models
from user.models import CustomUser
from book.models import Book
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Review(models.Model):
  user = models.ForeignKey(CustomUser, related_name="user_reviews", on_delete=models.CASCADE)
  book = models.ForeignKey(Book, related_name="book_reviews", on_delete=models.CASCADE)
  liked_by = models.ManyToManyField(CustomUser, related_name="liked_reviews", blank=True)
  written_text = models.CharField(max_length=300)
  star_rating = models.IntegerField(validators=[
        MinValueValidator(1),
        MaxValueValidator(5)
    ], null=True)
  spoiler = models.BooleanField(default=False)
  approved = models.BooleanField(default=False)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  def __str__(self):
    return f"{self.user}, {self.book}"
    