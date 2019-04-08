from django import forms
from .models import Comment,Essay_Comment




class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'url', 'text']
        widgets = {
            'name' :forms.TextInput(attrs={'class':'form-control','padding':'2px'}),
            'email' :forms.TextInput(attrs={'class':'form-control'}),
            'url' : forms.TextInput(attrs={'class':'form-control'}),
            'text': forms.Textarea(attrs={'cols': 80, 'rows': 3 ,'class':'form-control'}),
        }

class Essay_CommentForm(forms.ModelForm):
    class Meta:
        model = Essay_Comment
        fields = ['name', 'email', 'url', 'text']
        widgets = {
            'name' :forms.TextInput(attrs={'class':'form-control','padding':'2px'}),
            'email' :forms.TextInput(attrs={'class':'form-control'}),
            'url' : forms.TextInput(attrs={'class':'form-control'}),
            'text': forms.Textarea(attrs={'cols': 80, 'rows': 3 ,'class':'form-control'}),
        }


