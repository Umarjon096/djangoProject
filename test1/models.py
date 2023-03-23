from django.db import models

class Monitor(models.Model):
    name = models.CharField(max_length=50)

class File(models.Model):
    name = models.CharField(max_length=50)
    file = models.FileField(upload_to='files/')
    monitor = models.ForeignKey(Monitor, on_delete=models.CASCADE)
    duration = models.IntegerField(default=15)
    order = models.IntegerField(default=0)

