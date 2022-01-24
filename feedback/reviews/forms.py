from cProfile import label
from django import forms

from .models import Review

# class ReviewForm(forms.Form):
#     first_name = forms.CharField(label="First Name", max_length="100", error_messages={
#         "required": "First Name can't be empty!",
#         "max_length": "Please enter a shorter name!"
#     })
#     last_name = forms.CharField(label="Last Name", required="False", max_length="100", error_messages={
#         "max_length": "Please enter a shorter name!"
#     })
#     review = forms.CharField(label="Feedback", widget=forms.Textarea, max_length=200)
#     rating = forms.IntegerField(label="Rating", min_value=1, max_value=5) 

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review

        # fields = ['first_name', 'last_name', 'review', 'rating']
        fields = '__all__'
        # exlude = ['last_name']

        labels = {
            "first_name": "First Name",
            "last_name": "Last Name",
            "review": "Review",
            "rating": "Rating"
        }

        error_messages = {
            "first_name": {
                "required": "First Name can't be empty!",
                "max_length": "Please enter a shorter name!"
            },
            "last_name": {
                "required": "Last Name can't be empty!",
                "max_length": "Please enter a shorter name!"
            }
        }