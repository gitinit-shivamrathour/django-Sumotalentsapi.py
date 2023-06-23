from django.db import models
from django.contrib.auth.models import User

class Notes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=100)
    desc = models.TextField()
    audio = models.FileField(null=True, blank=True, upload_to="audio")
    video = models.FileField(null=True, blank=True, upload_to="video")
