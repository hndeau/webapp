from django.db import models


class UploadedMedia(models.Model):
    name = models.CharField(max_length=255)
    state = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "file"

    def __str__(self):
        return self.name
