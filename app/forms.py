from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import ProductUser

class ProductUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = ProductUser
        fields = ('__all__')