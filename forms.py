from django import forms
from website.models import Create
from django.forms import TextInput, FileInput


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Create
        fields = "__all__"
        widgets = {
            'Title': TextInput(attrs={'class': "form-control form-control-lg",
                                      'id': "exampleFormControlInput1",
                                      'placeholder': "Title of Booklet"}),
            'Author': TextInput(attrs={'class': "form-control",
                                       'id': "exampleFormControlInput1",
                                       'placeholder': "Author"}),
            'Comment':  TextInput(attrs={'class': "form-control",
                                         'id': "exampleFormControlTextarea1",
                                         'placeholder': "What is it about !!",
                                         'style': 'height :200px;'}),
            'File': FileInput(attrs={'class': "form-control",
                                     'id': "formFile"})
        }
