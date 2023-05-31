from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic.edit import UpdateView, DeleteView
from core.views import AbstractList
from .forms import CreateRequestForm, EditUserRequest
from core.models import Request, CreatorRequestExecutor


class AllRequests(AbstractList):
    model = CreatorRequestExecutor
    template_name = 'requests/list.html'
    fields = ['Creator', 'Name', 'Description',
              'Executor', 'Status', 'Created', 'Deadline']

    def patch_context(self):
        try:
            super().patch_context()
            data = self.model.objects.select_related("creator",
                                                     "executor",
                                                     "request")
            self.context["data"] = data
        finally:
            pass


class MyRequests(AbstractList):
    model = CreatorRequestExecutor
    template_name = 'requests/requests.html'
    fields = ['Name', 'Description',
              'Executor', 'Status', 'Deadline']

    def patch_context(self):
        try:
            super().patch_context()
            data = self.model.objects.select_related("creator",
                                                     "executor",
                                                     "request"
            ).filter(creator=self.request.user)
            self.context["data"] = list(data)
        finally:
            pass


class PendingRequests(AbstractList):
    model = CreatorRequestExecutor
    template_name = 'requests/pending_requests.html'
    fields = ['Creator', 'Name', 'Description',
              'Status', 'Created', 'Deadline']

    def patch_context(self):
        try:
            super().patch_context()
            data = self.model.objects.select_related("request",
                                                     "creator"
            ).filter(executor=self.request.user)
            self.context["data"] = list(data)
        finally:
            pass


class CreateRequest(CreateView):
    form_class = CreateRequestForm
    template_name = 'requests/create.html'

    def form_valid(self, form):
        form = form.save()
        cer = CreatorRequestExecutor(creator=self.request.user,
                                     executor=None,
                                     request=form,
                                     deadline=None,
                                     status='1')
        cer.save()
        return redirect('requests:my_requests')


class EditRequest(UpdateView):
    model = CreatorRequestExecutor
    form_class = EditUserRequest
    template_name = 'requests/edit.html'

    def form_valid(self, form):
        self.object.status = '2'
        form.save()
        return redirect('requests:list')


class DeleteUserRequest(DeleteView):
    model = Request

    def get_success_url(self) -> str:
        return reverse_lazy('requests:list')


def complete_request(request, pk):
    cre = CreatorRequestExecutor.objects.get(id=pk)
    cre.status = '3'
    cre.save()
    return redirect('requests:list')
