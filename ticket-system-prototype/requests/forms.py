from django import forms
from django.forms import ModelForm
from core.models import Request, CreatorRequestExecutor


class CreateRequestForm(ModelForm):

    class Meta:
        model = Request
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': "form-control"}),
            'description': forms.Textarea(attrs={'class': "form-control"})
        }


class EditUserRequest(ModelForm):

    class Meta:
        model = CreatorRequestExecutor
        fields = ['executor', 'deadline']
        widgets = {
            'executor': forms.Select(attrs={'class': "form-control"}, ),
            'deadline': forms.SelectDateWidget(attrs={'class': "form-control"}),
        }
