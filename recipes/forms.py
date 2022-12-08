from django import forms 
from .models import Comments


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        exclude = ["recipe"]

        labels = {
            "user_name": "Name",
            "comment":"Add Comment"
        }

        error_messages ={
            "user_name" : {
                "required":"Please Provide Your Name",
                "max_length":"Maximum Legth Exceeds"
            },
            "comment":{
                "required":"Commenting is must",
                "max_length":"Please do not exceed maximum length"
            }

        }
