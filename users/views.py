from django.shortcuts import render, redirect
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.forms import PasswordInput
class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True, help_text='',label='E-mail*')
    username = forms.CharField(max_length=20, help_text='',label='Введіть ваш логін')
    password1 = forms.CharField(max_length=20, help_text='',label='Пароль',widget=PasswordInput())
    password2 = forms.CharField(max_length=20, help_text='',label='Підтвердити пароль',widget=PasswordInput())
    first_name = forms.CharField(max_length=20, required=True, label="Ваше Ім'я")
    last_name = forms.CharField(max_length=20, required=True, label="Ваше Прізвище")
    phone_number = forms.CharField(
        max_length=20, required=True, label="Номер телефону",
        widget=forms.TextInput(attrs={'placeholder': '+380', 'value': '+380'})
    )

    class Meta:
        model = User
        fields = (
            'first_name',
            'last_name',
            'phone_number',
            'username',
            'email',
            'password1',
            'password2',
        )
        widgets = {
            'password1': PasswordInput(),
            'password2': PasswordInput(),
        }
    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            # Выполнение входа и перенаправление на домашнюю страницу.
            login(request, new_user)
            return redirect('Druk_site_app:index')
    else:
        form = RegistrationForm()

    return render(request, 'registration/register.html', {'form': form})