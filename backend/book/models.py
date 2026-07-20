from django.db import models
 
# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    cover = models.ImageField(upload_to='profile_pics/')
    avg_star_rating = models.IntegerField(min=1, max=5, null=True)
    genres = models.JSONField()
    archived = models.BooleanField(default=False)

    def __str__(self):
        return self.title
    