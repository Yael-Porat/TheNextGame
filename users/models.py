from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=20, choices=[
        ('admin', 'Admin'),
        ('editor', 'Editor'),
        ('signed', 'Signed'),
    ])

    def __str__(self):
        return f"{self.user.username} - {self.role}"

