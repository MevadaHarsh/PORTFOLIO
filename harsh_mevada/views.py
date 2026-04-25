from django.shortcuts import render
from .models import *
from django.core.mail import send_mail
from django.conf import settings    

# Create your views here.

def index(request):
    if request.method == 'POST':
        name=request.POST['name']
        email=request.POST['email']
        subject = request.POST.get('subject')
        message=request.POST['message']

        created=ContactUs.objects.create(
            name=name,
            email=email,
            message=message
        )
        
        send_mail(
            subject="Thanks for contacting me",
            message=f"""
Hi {name},
Thank you for reaching out. I’ve received your message and will get back to you soon.
            
Best regards,
Harsh Mevada
""",
            recipient_list=[email],
            from_email= settings.EMAIL_HOST_USER,
            fail_silently=False
        )
        
        send_mail(
            subject,
            message,
            recipient_list=[settings.EMAIL_HOST_USER],
            from_email= settings.EMAIL_HOST_USER,
            fail_silently=False
        )
        created.save()
        
    return render(request, 'index.html')