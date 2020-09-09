from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Links(models.Model):
    link = models.CharField(max_length=400, blank=False, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_links")
    status = models.CharField(default=None, blank=True, null=True, max_length=20)
    last_sync = models.DateTimeField(default=None, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.link
