from django import forms
from .models import Toss


class SentForm(forms.ModelForm):
    class Meta:
        model = Toss
        fields = ['toss']

    def pure_toss(self):
        return self.cleaned_data['toss']
