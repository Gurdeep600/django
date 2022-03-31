
import email
from multiprocessing import context
from django.shortcuts import render, HttpResponse
from home.models import Contact

# Create your views here.
def index(request):
    context = {
        "variable": "this is sent"
    }
    return render(request, 'index.html', context)
 
def about(request):
    return render(request, 'about.html')

def service(request):
    return render(request, 'services.html')

def contactus(request):
    if request.method == "POST":
        email = request.POST.get('email') 
        phone = request.POST.get('phone')
        contactus= Contact(email=email , phone=phone)
        contactus.save()
    return render(request, 'contact.html')
