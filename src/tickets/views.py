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

    def check_failed(self):
        self.model.objects.filter(status=Statuses.SUBMIT,
                                  deadline__lt=date.today()).update(status=Statuses.FAIL)

    def patch_context(self):
        self.context['fields'] = self.fields

    def get_context_data(self, **kwargs):
        self.context = super().get_context_data(**kwargs)
        self.patch_context()
        self.check_failed()

        return self.context


class AllTickets(AbstractList):
    model = Ticket
    template_name = 'tickets/all_tickets.html'
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
    template_name = 'tickets/my_tickets.html'
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
    template_name = 'tickets/pending_tickets.html'
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
    template_name = 'tickets/create_tickets.html'

    def form_valid(self, form):
        form = form.save()
        ticket = Ticket(creator=self.request.user,
                        executor=None,
                        request=form,
                        deadline=None,
                        status=Statuses.HOLD)
        ticket.save()
        return redirect('tickets:all_tickets')


class EditTicket(UpdateView):
    model = Ticket
    form_class = EditTicketForm
    template_name = 'tickets/edit_tickets.html'

    def form_valid(self, form):
        self.object.status = Statuses.SUBMIT
        form.save()
        return redirect('tickets:all_tickets')


class DeleteTicket(DeleteView):
    model = Request

    def get_success_url(self):
        return reverse_lazy('tickets:all_tickets')


def complete_ticket(request, pk):
    ticket = Ticket.objects.get(id=pk)
    ticket.status = Statuses.COMPLETE
    ticket.save()
    return redirect('tickets:all_tickets')
