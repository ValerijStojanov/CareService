from django.shortcuts import render

def landing_page(request):
    return render(request, 'landing_page.html')


    
def home(request):
    return render(request, 'home.html')
