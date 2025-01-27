from django.shortcuts import render,redirect
from steveApp.models import Contacts

# Create your views here.

def home(request):
    return render(request,'index.html')

def contacts(request):
    if request.method == 'POST':
        client_name = request.POST['client_name']
        client_email = request.POST['client_email']
        client_message = request.POST['client_message']

        client = Contacts(
            client_name=client_name,
            client_email=client_email,
            client_message = client_message
        )

        client.save()
    return redirect('/')

def view_contacts(request):
    contact =Contacts.objects.all()

    return render(request,'view_contacts.html',{'contacts':contact})
