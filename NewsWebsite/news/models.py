from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

class AppUser(models.Model):
    name = models.CharField(max_length=120)
    surname = models.CharField(max_length=120)
    info = models.TextField(blank=True, null=True)

    def __str__(self):
        return f'{self.name} {self.surname}'


class Article(models.Model):
    writer = models.ForeignKey(AppUser, on_delete=models.CASCADE, related_name='articles')
    title = models.CharField(max_length=120)
    description = models.CharField(max_length=200)
    text = models.TextField()
    city = models.CharField(max_length=120)
    publication_date = models.DateField()
    active = models.BooleanField(default=True)
    creation_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    
class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
   # commenter = models.CharField(max_length=250) 
    commenter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_comments')
    comment = models.TextField(blank=True, null=True) 
    creation_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)
    rating = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)],
    )

    def __str__(self):
        return str(self.rating)
