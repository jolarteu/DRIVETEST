from django import forms
from drive.models import drivetest

class DateInput(forms.DateInput):
    input_type = 'date'

class  driveForm(forms.ModelForm):

    class Meta:

        model = drivetest
        fields= ['name','csv','date', 'kml', 'bill']

        widgets = {
            'date': DateInput(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[str(field)].widget.attrs.update({'class': 'form-control'})
