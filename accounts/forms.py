from django.contrib.auth.models import User
from django import forms
from .models import ProfilePhoto

class UserForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password']
        labels ={
            'Username': 'username',
            'Password': 'password'
        }

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Username',
                                                     'id': 'username'})
        self.fields['password'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Password',
                                                     'id': 'password'})


class PhotoForm(forms.ModelForm):

    class Meta:
        model = ProfilePhoto
        exclude = ['userPhoto']
