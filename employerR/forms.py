from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        # fields = '__all__'
        fields = {'fullname','mobile', 'pmp_code', 'position'}
        labels = {
            'fullname': 'Full Name',
            'pmp_code': 'Emp Code',

        }
    
    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)
        self.fields['position'].empty_label= 'select option'
        self.fields['pmp_code'].required = False

