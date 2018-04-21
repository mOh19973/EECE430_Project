from django import forms
from testdrive.models import TDModel


class TDForm(forms.ModelForm):

    class Meta:
        model = TDModel
        exclude = ['driveDate']
