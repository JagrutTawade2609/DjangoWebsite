from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import customer, fooditem, reviews
class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=101)
    last_name = forms.CharField(max_length=101)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']
class customerForm(forms.ModelForm):
    class Meta:
        model = customer
        fields = '__all__'
        widgets = {
            'username': forms.TextInput(attrs={'class':"form-control"}),
            'useraddress': forms.TextInput(attrs={'class':"form-control"})
        }
class fooditemForm(forms.ModelForm):
    class Meta:
        model = fooditem
        fields = '__all__'
        widgets = {
            'foodname': forms.TextInput(attrs={'class':"form-control"}),
            'picture': forms.FileInput(attrs={'class':"form-control"}),
            'foodprice': forms.NumberInput(attrs={'class':"form-control"}),        
            'foodtype': forms.TextInput(attrs={'class':"form-control"})
        }
class reviewForm(forms.ModelForm):
    class Meta:
        model = reviews
        fields = '__all__'
        widgets = {
            'foodid': forms.Select(attrs={'class':"form-control"}),
            'reviewername': forms.Select(attrs={'class':"form-control"}),
            'rating': forms.NumberInput(attrs={'class':"form-control"})
        }
