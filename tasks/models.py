from django.db import models
from django.contrib.auth.models import User

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    date = models.DateField(auto_now_add=True)
    hours_spent = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.title} ({self.user.username})"
