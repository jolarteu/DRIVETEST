from django import forms

from drive.models import drivetest


class  driveForm(forms.ModelForm):

    class Meta:

        model = drivetest
        fields= ['name','uploadedFile']
