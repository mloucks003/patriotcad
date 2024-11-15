# forms.py
from django import forms
from .models import Call
from django.contrib.auth.models import User

class AssignOfficerForm(forms.ModelForm):
    class Meta:
        model = Call
        fields = ['assigned_officer']  # Ensure this field exists in the Call model

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Correct the field name to match the one defined in the model
        self.fields['assigned_officer'].queryset = User.objects.filter(is_active=True)  # Only active users