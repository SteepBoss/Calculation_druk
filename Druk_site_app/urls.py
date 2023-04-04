from django.urls import path
from . import views

app_name = 'Druk_site_app'
urlpatterns = [
    path('', views.index, name='index'),
]