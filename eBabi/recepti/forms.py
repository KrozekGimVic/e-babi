from django import forms

from .models import Recipe

class CompareForm(forms.Form):
    r1 = forms.ModelChoiceField(queryset=Recipe.objects.all())
    r2 = forms.ModelChoiceField(queryset=Recipe.objects.all())

    def clean(self):
        super().clean()
        if self.errors:
            return

        r1 = self.cleaned_data['r1']
        r2 = self.cleaned_data['r2']
        if r1 == r2:
            raise forms.ValidationError('Primerjati je potrebno razlicne recepte.')
