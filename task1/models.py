from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()

    likes = models.ManyToManyField(User, related_name="likes", default=None, blank=True)
    slug = models.SlugField(blank=True, max_length=250)

    def get_absolute_url(self):

        return reverse("task1:post_single", args=[self.slug])

    def __str__(self) -> str:
        return self.title
