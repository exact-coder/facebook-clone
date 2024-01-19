from django.db import models
from apps.post.models import Post
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    text = models.TextField()
    updated_at = models.DateTimeField(_(""), auto_now=True, auto_now_add=False)

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    def __str__(self) -> str:
        return f'Comment by {self.author.username} on {self.post.title} post' # type: ignore

