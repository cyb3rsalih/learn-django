from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout,Submit

class SubmitForm(forms.Form):
    n1 = forms.FloatField(label=False);
    n2 = forms.FloatField(label=False);
    mean_1 = forms.FloatField(label=False);
    mean_2 = forms.FloatField(label=False);
    stdev_1 = forms.FloatField(label=False);
    stdev_2 = forms.FloatField(label=False);


class ChisForm(forms.Form):
    a = forms.FloatField(label=False, widget=forms.TextInput(attrs={'placeholder': 'a'}));
    b = forms.FloatField(label=False, widget=forms.TextInput(attrs={'placeholder': 'b'}));
    c = forms.FloatField(label=False, widget=forms.TextInput(attrs={'placeholder': 'c'}));
    d = forms.FloatField(label=False, widget=forms.TextInput(attrs={'placeholder': 'd'}));
    
    # def __init__(self,*args,**kwargs):
    #     super().__init__(*args,**kwargs)
    
    #     self.helper = FormHelper
    #     self.helper.form_method = 'post'
    #     self.helper.disable_csrf = True

    #     self.helper.layout = Layout(
    #         'n1',
    #         'n2',
    #         'mean_1',
    #         'mean_2',
    #         'stdev_1',
    #         'stdev_2',
    #         Submit('submit','Calculate',css_class='btn-success m-2')
    #     )
    
