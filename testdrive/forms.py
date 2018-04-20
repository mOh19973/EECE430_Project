from django import forms

class TDForm(forms.Form):
    username = forms.CharField(label='username')
    carName = forms.CharField(label='carName')
    day = forms.IntegerField(label='day')
    month = forms.IntegerField(label='month')
    year = forms.IntegerField(label='year')
    hour = forms.IntegerField(label='hour')
    minutes = forms.IntegerField(label='minutes')

