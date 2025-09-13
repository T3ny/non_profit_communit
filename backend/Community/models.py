from django.db import models
from django.conf import settings


# Groups & Events
class Group(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    members = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='communty_groups')

    def __str__(self):
        return self.name

class Event(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='events')
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return f"{self.title} - {self.group.name}"

# Create your models here.
