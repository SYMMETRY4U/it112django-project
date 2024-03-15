# forms.py

from django import forms
from .models import Invention

class InventionForm(forms.ModelForm):
    class Meta:
        model = Invention
        fields = ['name', 'inventor', 'year', 'description', 'background', 'outcome', 'category']
