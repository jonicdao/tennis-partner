from django import forms
from django.forms import ModelForm
from .models import Partner

class PostForm(forms.ModelForm):

    class Meta:
        model = Partner
        fields = ('first_name', 'last_name', 'level', 'zipcode', 'email', 'description')