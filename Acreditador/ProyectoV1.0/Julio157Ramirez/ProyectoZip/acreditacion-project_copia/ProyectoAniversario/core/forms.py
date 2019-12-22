from django import forms

class AsistenteForm(forms.Form):
    text = forms.CharField(max_length=255,
        widget=forms.TextInput(
            attrs={'class' : 'form-control mr-sm-2','type': 'search','id': 'inputSearch', 'value': '', 'placeholder' : 'RUN o Nombre', 'aria-label' : 'Search', 'autofocus': 'true'}))


