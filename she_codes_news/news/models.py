from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

class NewsStory(models.Model):
    title = models.CharField(max_length=200)
    # author = models.CharField(max_length=200)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE
    )
    pub_date = models.DateTimeField(default=timezone.now)
    content = models.TextField()
    image_url = models.URLField(null=True)
    favorites = models.ManyToManyField("users.CustomUser", related_name="favorites", default=None, blank=True)

