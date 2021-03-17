from django.core import validators
from django import forms
from django.forms import fields, widgets
from .models import User
class StudentRegistration(forms.ModelForm):
    class Meta:
        model = User
        fields= "__all__"
        widgets={
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'contact':forms.TextInput(attrs={'class':'form-control'}),
            'course':forms.TextInput(attrs={'class':'form-control'}),
            'city':forms.TextInput(attrs={'class':'form-control'}),
        }