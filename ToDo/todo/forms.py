from django import forms
from .models import Todo


class ListForm(forms.ModelForm):
    class Meta:
        model=Todo
        fields = ["title" , "description" ,"completed" ,"date"]