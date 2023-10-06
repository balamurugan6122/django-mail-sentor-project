from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.conf import settings

def send_email(request):
    if request.method == 'POST':
        recipient_email = request.POST.get('recipient_email')
        email_message = request.POST.get('email_message')

        if recipient_email and email_message:
            subject = 'Email Subject'
            message = email_message
            from_email = 'rbalamurugan61222@gmail.com'  # Replace with your email address
            recipient_list = [recipient_email]

            send_mail(subject, message, from_email, recipient_list)
            return redirect('email_sent')

    return render(request, 'email_form.html')

def email_sent(request):
    return render(request, 'email_sent.html')