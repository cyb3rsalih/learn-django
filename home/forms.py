from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout,Submit

class SubmitForm(forms.Form):
    n1 = forms.FloatField();
    n2 = forms.FloatField();
    m1 = forms.FloatField();
    m2 = forms.FloatField();
    s1 = forms.FloatField();
    s2 = forms.FloatField();


    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
    
        self.helper = FormHelper
        self.helper.form_method = 'post'

        self.helper.layout = Layout(
            'n1',
            'n2',
            'm1',
            'm2',
            's1',
            's2',
            Submit('submit','Calculate',css_class='btn-success m-2')
        )
    
