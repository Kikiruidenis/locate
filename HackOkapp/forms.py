from django import forms
from . models import Lost,Found

class LostForm(forms.ModelForm):
    class Meta:
        model = Lost
        fields = ('user','name','age','gender','clothes_color','complexion', 'contact','child_pic')

class FoundForm(forms.ModelForm):
    class Meta:
        model= Found
        fields= ['location','contact', 'videofile']