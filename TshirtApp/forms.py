from django import forms
from TshirtApp.models import Tshirts,Orders
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class Registration(UserCreationForm):
    gmail=forms.EmailField(required=True)
    class Meta:
        model=User
        fields=['username','email','password_1','password_2']


class Tshirt_form(forms.ModelForm):
    class Meta:
        model=Tshirts
        fields='__all__'


class Order_form(forms.ModelForm):
    class Meta:
        model=Orders
        fields='__all__'
