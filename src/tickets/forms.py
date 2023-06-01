from django import forms
from django.forms import ModelForm
from .models import Request, Ticket


class CreateTicketForm(ModelForm):

    class Meta:
        model = Request
        fields = ['name', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': "form-control"}),
            'description': forms.Textarea(attrs={'class': "form-control"})
        }


class EditTicketForm(ModelForm):

    class Meta:
        model = Ticket
        fields = ['executor', 'deadline']
        widgets = {
            'executor': forms.Select(attrs={'class': "form-control"}, ),
            'deadline': forms.SelectDateWidget(attrs={'class': "form-control"}),
        }
