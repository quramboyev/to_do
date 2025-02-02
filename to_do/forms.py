from string import digits
from django import forms
from .models import ToDoModel

class EditTodoForm(forms.ModelForm):
    text = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'bg-info-subtle',
        'placeholder': 'Enter your text',
        'required': 'True',
    }), required=False)
    class Meta:
        model = ToDoModel
        exclude = ['is_active']
        labels = {
            'title': "a",
            'description': "descript",
        }
        widgets = {
            'title': forms.Textarea(attrs={
                'class': 'bg-secondary',
                'placeholder': 'ASA'
            }),
            'description': forms.Textarea(attrs={
                'class': 'bg-dark-subtle',
                'placeholder': 'info'
            })
        }

class CreateTodoForm(forms.Form):
     title = forms.CharField(max_length=100, min_length=3, label='Title', widget=forms.TextInput(
         attrs={'placeholder': 'Title'}))
     description = forms.CharField(widget=forms.Textarea(
         attrs={'placeholder': 'Description'}))
     price = forms.DecimalField(label='Price',widget=forms.NumberInput(attrs={'placeholder': 'Price'}),
         max_digits=10, decimal_places=2
     )
