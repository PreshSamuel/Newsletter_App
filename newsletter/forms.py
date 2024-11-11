from django import forms
from .models import SubUsers, newsletter

class SubForm(forms.ModelForm):
    class Meta:
        model = SubUsers
        fields = ['email']

class AddLetter(forms.ModelForm):
    title = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Title", "class":"form-control"}), label="")
    body = forms.CharField(required=True, widget=forms.widgets.TextInput(attrs={"placeholder":"Enter Text", "class":"form-control"}), label="")
    class Meta:
        model = newsletter
        fields = '__all__'
