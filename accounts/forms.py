from django.contrib.auth.models import User
from django import forms


class UserForm(forms.ModelForm):

    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password']
        labels ={
            'username': 'username',
            'password': 'password'
        }

    def __init__(self, *args, **kwargs):
        super(UserForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Username',
                                                     'id': 'username',
                                                     'style': 'margin-bottom: -1px; '
                                                              'border-bottom-right-radius: 0; '
                                                              'border-bottom-left-radius: 0; '
                                                              'border-top-left-radius: 0; '
                                                              'border-top-right-radius: 0;'})
        self.fields['password'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Password',
                                                     'id': 'password'})
