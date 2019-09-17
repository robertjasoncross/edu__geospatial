from django import forms
from .models import Arenas

class ArenaForm(forms.Form):
    name=""
    description = "Use the drop down fucker"
    selections = forms.ChoiceField(choices=Arenas.objects.values_list('id', 'name1'), widget=forms.Select(), required=True)
