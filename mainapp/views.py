from django.shortcuts import render,redirect
from django.conf import settings
from django.core.mail import send_mail
from django.contrib import messages


# Create your views here.
def home(request):
    if request.method=="POST":
        name=request.POST.get('name')
        email=request.POST.get('email')
        message=request.POST.get('message')
        message1 = f'Hi {name}, thank you for contacting, I will get back you soon...'
        email_from = settings.EMAIL_HOST_USER
        recipient_list = [email, ]
        # try:
        send_mail("Message received", message1, email_from, recipient_list )
        recipient_list = [email_from, ]
        message1 = f'Query from :- {name}\nEmail id :- {email}\nMessage :- {message}'
        send_mail("Query", message1, email_from, recipient_list)
        messages.success(request, 'Message sent successfully!!!')
        # except:
        # messages.success(request, 'Message not sent please try after some time!!!')
        return redirect('home')
    return render(request, 'mainapp/homepage.html')