from django.db import models
import datetime

class Data(models.Model):
    created_time = models.DateTimeField(auto_now_add=True)
    value = models.FloatField()
