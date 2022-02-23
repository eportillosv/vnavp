from dataclasses import fields
from django import forms
from .models import User

class UsersForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'