from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail

# Create your views here.
def base_view(request, *args, **kwargs):
    if request.method == "POST":
        first_name = request.POST['first-name']
        last_name = request.POST['last-name']
        email = request.POST['email']
        message = request.POST['message']

        # send an email
        send_mail(
            'Message from ' + first_name + ' ' + last_name, # subject
            message, # message
            email, # from email
            ['nathaniel.chang828@gmail.com'], # to email
        )

        return render(request, 'base.html', {'first_name' : first_name})
    else:
        return render(request, 'base.html', {})