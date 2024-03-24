from django import forms
from .models import UserReview

#the forms create a text input fields
# class UserReviewForm(forms.Form):
#     user_name = forms.CharField(label="Your Name", max_length=100, error_messages={
#         'required':'Your name must not be empty!',
#         'max_length':'Please enter shorter name!'
#     })  
#     # _ give space on the forms, label(is use to change the name), max_length or min_length(to give the length of text),error_messages(to change the error message) setting required to=False disable the required.
#     review_text = forms.CharField(label='Your Feedback', widget=forms.Textarea, max_length=200)
#     rating = forms.IntegerField(label="Your Rating", min_value=1, max_value=5)


#second to crate a form.

class UserReviewForm(forms.ModelForm):
    class Meta:
        model = UserReview
        #fields = ['user_name', 'review_text', 'rating'] #the fields is to show the field that will be display
        fields = '__all__' #it shows all the fields to be display
        #exclude = ['owner_comment'] #it show field that will not be display to the end user.
        labels = {
            'user_name': 'Your Name',
            'review_text': 'Your Feedback',
            'rating': 'Your Rating'
        }
        error_messages = {
            'user_name': {
                'required':'Your name must not be empty!',
                'max_length':'Please enter shorter name!'
            }
        }