from django import forms


class CommentForm(forms.Form):
    author_name = forms.CharField(max_length=32, widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'Username',
        "id": "username",
        "name": "username",
    }), required=True)
    author_email = forms.EmailField(widget=forms.TextInput(attrs={
        'class': 'form-control',
        'placeholder': 'your@email.com',
        "id": "email",
        "name": "email",
    }), required=True)
    content = forms.CharField(max_length=256, widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Your comment',
        "id": "content",
        "name": "content",
        "rows": 3
    }))
