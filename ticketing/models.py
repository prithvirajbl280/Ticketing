from django.contrib.auth.models import User
from django.db import models

class Registration(models.Model):
    YEAR_CHOICES = [
        ('1st Year', '1st Year'),
        ('2nd Year', '2nd Year'),
        ('3rd Year', '3rd Year'),
        ('4th Year', '4th Year'),
        ('Graduated', 'Graduated'),
    ]
    name = models.CharField(max_length=100)
    srn = models.CharField(max_length=50)
    prn = models.CharField(max_length=50, blank=True, null=True)
    year = models.CharField(max_length=20, choices=YEAR_CHOICES)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.srn})"


class TicketConfirmation(models.Model):
    PAYMENT_CHOICES = [
        ('Cash', 'Cash'),
        ('UPI', 'UPI'),
    ]
    student = models.ForeignKey(Registration, on_delete=models.CASCADE)
    payment_type = models.CharField(max_length=10, choices=PAYMENT_CHOICES)
    utr_number = models.CharField(max_length=100, blank=True, null=True)
    confirmed_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, limit_choices_to={'groups__name': 'Organiser'})
    confirmed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Ticket for {self.student.name} confirmed by {self.confirmed_by.username}"
