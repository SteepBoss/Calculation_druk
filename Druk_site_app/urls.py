from django.urls import path
from . import views

app_name = 'Druk_site_app'
urlpatterns = [
    path('', views.index, name='index'),
    path('registration', views.registration),
    path('write_us', views.write_us),
]