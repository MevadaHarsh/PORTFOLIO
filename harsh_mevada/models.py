from django.db import models

# Create your models here.

class ContactUs(models.Model):
    SUBJECT_CHOICES = [
        ('internship', 'Internship Opportunity'),
        ('fresher', 'Fresher Job Role'),
        ('other', 'Other'),
    ]
    
    name=models.CharField(max_length=100, null=True, blank=True)
    email=models.CharField(max_length=100, null=True, blank=True)
    subject=models.CharField(max_length=500, choices=SUBJECT_CHOICES, default='other')
    message=models.TextField()

    def __str__(self):
        return self.name
    