from django import forms
from django.forms import ModelForm
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

User = get_user_model()


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Login',
                               widget=forms.TextInput(
                                   attrs={'class': "form-control"}))
    password = forms.CharField(label='Password',
                               widget=forms.PasswordInput(
                                   attrs={'class': "form-control"}))


class RegisterUserForm(UserCreationForm):
    password1 = forms.CharField(label='Password',
                                widget=forms.PasswordInput(
                                    attrs={'class': "form-control"}))
    password2 = forms.CharField(label='Repeat Password',
                                widget=forms.PasswordInput(
                                    attrs={'class': "form-control"}))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1']
        widgets = {
            'username': forms.TextInput(attrs={'class': "form-control"}),
            'email': forms.EmailInput(attrs={'class': "form-control"}),
            'password1': forms.PasswordInput(attrs={'class': "form-control"}),
        }


class EditUserForm(ModelForm):

    class Meta:
        model = User
        fields = ['username', 'email']
        widgets = {
            'username': forms.TextInput(attrs={'class': "form-control"}),
            'email': forms.EmailInput(attrs={'class': "form-control"}),
        }
