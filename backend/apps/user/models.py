from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
def user_image(instance, filename):
    return f"user/{instance.id}/{filename}"

class User(AbstractUser):
    email = models.EmailField(unique=True)
    image = models.ImageField(upload_to=user_image)
    bio = models.TextField(blank=True,null=True)

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self) -> str:
        return self.username
    
    @property
    def posts(self):
        return self.post_set.all() # type: ignore
