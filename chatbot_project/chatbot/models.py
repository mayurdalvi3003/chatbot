from django.db import models

class JSONData(models.Model):
    name = models.CharField(max_length=50)
    data = models.JSONField()
