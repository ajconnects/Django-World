from django import forms


class UserReviewForm(forms.Form):
    user_name = forms.CharField()
    password = forms.CharField()