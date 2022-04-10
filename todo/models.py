from django.db import models
from django.db.models.functions import Lower


class Tasks(models.Model):
    task = models.CharField(max_length=200)
    order = models.PositiveSmallIntegerField()

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.task
