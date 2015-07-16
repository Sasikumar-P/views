from django import forms
from .models import Demo, Demo1,Demo2

class DemoForm(forms.ModelForm):
    class Meta:
        model = Demo
        fields = ('field',)
class Demo1Form(forms.ModelForm):
    class Meta:
        model= Demo1
        fields=('field',)
class Demo2Form(forms.ModelForm):
    class Meta:
        model= Demo2
        fields=('field',)


