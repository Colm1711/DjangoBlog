from .models import Comment
from django import forms


class CommmentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)
