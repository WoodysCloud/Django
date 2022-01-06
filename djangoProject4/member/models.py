from django.db import models

# Create your models here.
class memberTable(models.Model):
    userid = models.CharField(max_length=200)
    userpw = models.CharField(max_length=200)
    username = models.CharField(max_length=200)
    usertel = models.CharField(max_length=100)

    def __str__(self):
        return self.username + ": " + self.userid + ", " + self.userpw + ", " + self.usertel
