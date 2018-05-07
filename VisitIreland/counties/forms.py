from django import forms
from .models import Attraction
from .models import Comment


class NewAttractionForm(forms.ModelForm):
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={'rows': 5, 'placeholder': 'What have you got to say?'}
        ),
        max_length=4000,
        help_text='The max length of the text is 4000.'
    )

    class Meta:
        model = Attraction
        fields = ['subject', 'message']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['message', ]