from django import forms

class LoginForm(forms.Form):
   username = forms.CharField(label='Username', max_length=100, widget=forms.TextInput(attrs={'class': 'form-control form-control-user', 'placeholder': 'Enter your username'}))
   password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-control form-control-user', 'placeholder': 'Enter your password'}))