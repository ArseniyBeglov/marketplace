from django.db import models
from django.contrib.postgres.fields import ArrayField


class Asset(models.Model):
    name = models.CharField(max_length=255, blank=True)
    description = models.TextField(blank=True)
    version = models.CharField(max_length=20, blank=True)
    archived = models.BooleanField(default=False)
    asset_link = models.URLField(blank=True)
    images_link = models.JSONField(blank=True, null=True)

    def __str__(self):
        return self.name