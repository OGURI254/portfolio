from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'index.html')
def about(request):
    return render(request, 'about.html')
def works(request):
    return render(request, 'works.html')
"""def contact(request):
    return render(request, 'contact.html')"""
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

from django.views.decorators.csrf import csrf_protect




from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact
from django.views.decorators.csrf import csrf_protect

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact

@csrf_protect
def contact(request):
    if request.method == 'POST':
        
        name = request.POST.get('full-name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

       
        try:
            Contact.objects.create(
                name=name,
                email=email,
                subject=subject,
                message=message
            )
            messages.success(request, 'Details successfully processed and saved.')
           
            return redirect('index') 
        except Exception as e:
            print(f'Error processing details: {str(e)}')
            messages.error(request, f'Error processing details: {str(e)}')

    return render(request, 'contact.html')



