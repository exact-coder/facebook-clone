from django.db import models
from apps.user.models import User


# Create your models here.
def upload_to(instance, filename):
    return f"post/{instance.id}/{filename}"

class Post(models.Model):
    description = models.TextField()
    image = models.ImageField(upload_to=upload_to)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.ManyToManyField(User, related_name="likes_set", blank=True,verbose_name='Likes')

    def __str__(self):
        return f"{self.author.username} - {self.id}" # type: ignore
    
    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        ordering = ["-created_at"]