from django.views.generic.list import ListView
from datetime import date
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic.edit import UpdateView, DeleteView
from .models import Request, Ticket

from .forms import CreateTicketForm, EditTicketForm
from .enum import Statuses


class AbstractList(ListView):
    context = {}
    fields = []

    def update_failed(self):
        self.model.objects.filter(status=Statuses.SUBMIT,
        deadline__lt=date.today()).update(status=Statuses.FAIL)

    def patch_context(self):
        self.context['fields'] = self.fields

    def get_context_data(self, **kwargs):
        self.context = super().get_context_data(**kwargs)
        self.patch_context()
        self.update_failed()

        return self.context


class AllTickets(AbstractList):
    model = Ticket
    template_name = 'requests/list.html'
    fields = ['Creator', 'Name', 'Description',
              'Executor', 'Status', 'Created', 'Deadline']

    def patch_context(self):
        super().patch_context()
        data = self.model.objects.select_related("creator",
                                                    "executor",
                                                    "request")
        self.context["data"] = data


class MyTickets(AbstractList):
    model = Ticket
    template_name = 'requests/requests.html'
    fields = ['Name', 'Description',
              'Executor', 'Status', 'Deadline']

    def patch_context(self):
        super().patch_context()
        data = self.model.objects.select_related("creator",
                                                    "executor",
                                                    "request"
        ).filter(creator=self.request.user)
        self.context["data"] = list(data)


class PendingTickets(AbstractList):
    model = Ticket
    template_name = 'requests/pending_requests.html'
    fields = ['Creator', 'Name', 'Description',
              'Status', 'Created', 'Deadline']

    def patch_context(self):
        super().patch_context()
        data = self.model.objects.select_related("request",
                                                    "creator"
        ).filter(executor=self.request.user)
        self.context["data"] = list(data)


class CreateTicket(CreateView):
    form_class = CreateTicketForm
    template_name = 'requests/create.html'

    def form_valid(self, form):
        form = form.save()
        cer = Ticket(creator=self.request.user,
                                     executor=None,
                                     request=form,
                                     deadline=None,
                                     status=Statuses.HOLD)
        cer.save()
        return redirect('requests:my_requests')


class EditTicket(UpdateView):
    model = Ticket
    form_class = EditTicketForm
    template_name = 'requests/edit.html'

    def form_valid(self, form):
        self.object.status = Statuses.SUBMIT
        form.save()
        return redirect('requests:list')


class DeleteTicket(DeleteView):
    model = Request

    def get_success_url(self) -> str:
        return reverse_lazy('requests:list')


def complete_ticket(request, pk):
    Ticket.objects.get(id=pk).update(status=Statuses.SUBMIT)
    return redirect('requests:list')
