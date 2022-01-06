import datetime

from django.db import models

# Create your models here.
class boardTable(models.Model):
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=200)
    writeDate = models.DateTimeField()

    def __str__(self):
        return self.title + ": " + self.content + " (" + str(self.writeDate) + ")"