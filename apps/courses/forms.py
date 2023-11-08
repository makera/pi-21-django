from django.forms import forms, fields


class CallbackForm(forms.Form):
    email = fields.EmailField()
    name = fields.CharField(min_length=10, max_length=50)
