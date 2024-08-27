from django.shortcuts import redirect, render
from .models import Resume


# Create your views here.
def home(request):
    resume = Resume.objects.first()
    return render(request, 'home.html', {'resume':resume})

def projects(request):
    return render(request, 'projects.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')


