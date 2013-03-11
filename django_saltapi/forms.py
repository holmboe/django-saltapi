# -*- coding: utf-8 -*-

from django import forms

class LowdataForm(forms.Form):
    client = forms.CharField(max_length=20,
                             initial='local',
                             widget=forms.HiddenInput())
    tgt    = forms.CharField(max_length=50,
                             label='Target')
    fun    = forms.CharField(max_length=30,
                             label='Module')
    arg    = forms.CharField(max_length=100,
                             required=False,
                             label='Arguments')

    def clean(self):
        cleaned_data = super(LowdataForm, self).clean()
        return cleaned_data

# class ModuleField(CharField):
#     default_error_messages = {
#         'invalid': _('A Salt module must have the form foo.bar.'),
#         }
#     default_validators = [validators.validate_email]
