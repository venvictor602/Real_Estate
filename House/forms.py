from django import forms
from django.contrib.auth.models import User

class  RegistrationForm(forms.ModelForm):
    password = forms.CharField(widget= forms.PasswordInput, label="Password")
    confirm_password = forms.CharField(widget= forms.PasswordInput, label="Confirm Password")

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'password']

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password != confirm_password:
            raise forms.ValidationError("passwords do not match")
        
        if User.objects.filter(email = cleaned_data.get('email')).exists():
            raise forms.ValidationError("Email already exist")
        
        return cleaned_data