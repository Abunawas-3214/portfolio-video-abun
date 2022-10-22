from django.db import models
from embed_video.fields import EmbedVideoField

# Create your models here.


class Content(models.Model):
    title = models.CharField(max_length=50)
    role = models.CharField(max_length=100)
    url = EmbedVideoField()

    def __str__(self):
        return "{}".format(self.title)
