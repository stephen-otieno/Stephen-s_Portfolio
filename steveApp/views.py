from django.contrib.auth.decorators import login_required
from django.shortcuts import render,redirect
from steveApp.models import Contacts
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .forms import CustomLoginForm


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

@login_required(login_url='login')
def view_contacts(request):
    contact =Contacts.objects.all()

    return render(request,'view_contacts.html',{'contacts':contact})

def login_page(request):
    if request.method == 'POST':
        form = CustomLoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('clients')  # Redirect to the clients page

            else:
                form.add_error(None, 'Invalid username or password')
    else:
        form = CustomLoginForm()
    return render(request, 'login.html', {'form': form})

    # return render(request, 'login.html')
