from django import forms
from .models import Sight

class SightForm(forms.ModelForm):

    class Meta():
        model = Sight
        fields = ('sight_title','sight_description','sight_lat','sight_lon',)
