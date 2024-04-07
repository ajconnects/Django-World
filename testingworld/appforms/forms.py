from django import forms
from .models import UserApplication


class UserApplicationForm(forms.ModelForm):
    class Meta:
        model = UserApplication
        fields = '__all__'

        labels = {
            "job_title": "Job Position",
            "rating" : "Company Rating",
            "phone" : "Phone Number",
            "date": "Application Date"
        }

        error_messages = {
            'job_title': { 
                'required': 'please the company name.',
            }
         }
        
        widgets = {
            'job_title': forms.TextInput(attrs={'class': 'form-control'}),
            'company': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'class': 'form-control'}),
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        }