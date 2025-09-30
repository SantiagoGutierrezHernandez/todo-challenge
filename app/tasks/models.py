from django.db import models
from django.contrib.auth.models import User


class TaskState(models.Model):
    name = models.CharField(max_length=30)
    user = models.ForeignKey(User, on_delete=models.CASCADE, editable=False, blank=False)


class Task(models.Model):
    title = models.CharField(max_length=100, blank=False)
    description = models.CharField(max_length=2000, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, editable=False, blank=False)
    state = models.ForeignKey(TaskState, on_delete=models.CASCADE)
    created_on = models.DateField(auto_now_add=True)
