
from django.shortcuts import render, redirect
def index(request):
    return render(request, 'Druk_site_app/index.html')

def write_us(request):
    return render(request, 'Druk_site_app/write_us.html')



