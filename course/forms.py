from django import forms
from django.contrib.auth.forms import AuthenticationForm
from accounts.models import User

from django import forms

class EnrollmentForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control', }))