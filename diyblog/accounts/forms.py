from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class SignUpForm(UserCreationForm):
    CHOICES  = [('1', 'Subscriber'), ('2', 'Author')]

    first_name = forms.CharField(max_length=30, required=False, help_text="Optional")
    last_name = forms.CharField(max_length=30, required=False, help_text="Optional")
    username = forms.CharField(max_length=30, required=True, help_text="Obligatory")
    email = forms.EmailField(max_length=254, required=True, help_text="Required. Input valid email adress")
    user_type = forms.ChoiceField(choices=CHOICES, required=True)

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'user_type', 'password1', 'password2']
