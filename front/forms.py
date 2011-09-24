from django import forms

class UrlizForm(forms.Form):
  url = forms.URLField(label='Website', initial='http://', widget=forms.TextInput(attrs={'size': '23'}))

