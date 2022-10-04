from pyexpat import model
from tkinter.tix import Form
from django import forms
from .models import Practice

class practiceForm(forms.ModelForm):

  class Meta:
    model = Practice
    fields = '__all__'