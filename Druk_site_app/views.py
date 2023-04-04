from django.shortcuts import render

def index(request):
    return render(request, 'Druk_site_app/index.html')


