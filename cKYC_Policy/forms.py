from django import forms
from django.forms.formsets import formset_factory
from .models import *

class PolicyFieldsForm(forms.Form):
    name = forms.CharField(required=True)
    meta = forms.ChoiceField(choices=FT_CHOICES)
    datatype = forms.ChoiceField(choices=DT_CHOICES)
    #widget=CheckboxSelectMultiple
    proof = forms.MultipleChoiceField(widget=forms.SelectMultiple,
    	choices=PD_CHOICES,required=False)
    pattern = forms.ChoiceField(choices=FT_CONSTRAINT_CHOICES,
        help_text='select data validations')
    message = forms.CharField(max_length=256,required=False)

PolicyFieldsFormset= formset_factory(PolicyFieldsForm)

class PolicyForm(forms.Form):
	policy_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
	policy_description = forms.CharField(widget=forms.Textarea(attrs={'rows': 8, 'cols': 107 }))
	policy_field= PolicyFieldsFormset()