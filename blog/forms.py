from django import forms

from .models import Comment




class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('author', 'text',)

        widgets = {
            'author': forms.TextInput(attrs={'class': 'textinputclass', 'placeholder':'Author'}),
            'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea', 'placeholder':'Comment'}),
        }
        

