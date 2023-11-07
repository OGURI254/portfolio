from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')
def about(request):
    return render(request, 'about.html')
def works(request):
    return render(request, 'works.html')
def contact(request):
    return render(request, 'contact.html')
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


