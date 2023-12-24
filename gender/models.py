from django.db import models

class UserBehavior(models.Model):
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]

    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    user_name = models.CharField(max_length=100)
    behavior = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.user_name} - {self.behavior}"
