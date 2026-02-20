from django import forms
from django.contrib.auth.forms import AuthenticationForm
from accounts.models import User

class LoginForm(forms.Form):
    username_or_email = forms.CharField(label='Username or Email',widget=forms.TextInput(attrs={'class':'form-control',}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))
    

class SignupForm(forms.ModelForm):
    password = forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control', "id":"nomd_deS8"}))
    password2 = forms.CharField(label='Repeat Password', widget=forms.PasswordInput(attrs={'class':'form-control',"id":"disci_R6"}))
    class Meta:
        model = User
        fields = ['username','first_name', 'last_name','email']
        widgets ={
        'username':forms.TextInput(attrs={'class':'form-control'}),
         'first_name':forms.TextInput(attrs={'class':'form-control'}),

          'last_name':forms.TextInput(attrs={'class':'form-control'}),
                
           'email':forms.EmailInput(attrs={'class':'form-control'}),
               
            }
    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']