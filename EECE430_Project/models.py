from django.db import models


class Apps(models.Model):
    link = models.CharField(max_length=500)
