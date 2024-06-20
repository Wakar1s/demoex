from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    ROLE_CHOICES = (
        ('manager', 'Manager'),
        ('room_service', 'Room Service Employee'),
        ('hotel_service', 'Hotel Service Provider'),
    )
    STATUS_CHOICES = (
        ('active', 'Active'),
        ('dismissed', 'Dismissed'),
    )
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    father_name = models.CharField(max_length=30, default='-')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='active')

class Order(models.Model):
    STATUS_CHOICES = (
        ('preparing', 'Preparing'),
        ('ready', 'Ready'),
    )
    PAYMENT_STATUS_CHOICES = (
        ('accepted', 'Accepted'),
        ('paid', 'Paid'),
    )
    created_by = models.ForeignKey(User, related_name='orders', on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='preparing')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    details = models.TextField()
    room_num = models.CharField(max_length=7, default=1)
    amount_clients = models.IntegerField(default=1)
    payment_status = models.CharField(max_length=20, choices=PAYMENT_STATUS_CHOICES, default='pending')
    

class Shift(models.Model):
    user = models.ForeignKey(User, related_name='shifts', on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()

    def __str__(self):
        return f"{self.user.username}: {self.start_time} - {self.end_time}"