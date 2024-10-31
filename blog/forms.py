from django import forms

from .models import Email
from .models import Contact

class EmailForm(forms.ModelForm):
    class Meta:
        model = Email
        fields = ['email',]

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name','bio', 'subject', 'contactemail']


