from django import forms

class ProfileFrom(forms.Form):
    user_image = forms.ImageField()