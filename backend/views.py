from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact

# Create your views here.
def index(request):
    return render(request, 'index.html')
def about(request):
    return render(request, 'about.html')
def works(request):
    return render(request, 'works.html')
def credentials(request):
    return render(request, 'credentials.html')
def blog(request):
    return render(request, 'blog.html')
def services(request):
    return render(request, 'service.html')
def blogdetails(request):
    return render(request, 'blogdetails.html')
def workdetails(request):
    return render(request, 'workdetails.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('full-name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        Contact.objects.create(
            name=name,
            email=email,
            subject=subject,
            message=message
        ).save()

        messages.success(request, 'Details successfully processed and saved.')
        print('\n\n\n We are seeing data being saved\n\n\n')
        return redirect('index') 
    
    print('\n\n\n We are seeing this because it did not direct\n\n\n')
    return render(request, 'contact.html')



