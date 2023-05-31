from django.views.generic.list import ListView
from datetime import date


class AbstractList(ListView):
    context = {}
    fields = []

    def update_failed(self):
        try:
            failed = self.model.objects.filter(status='2',
                                               deadline__lt=date.today())
            failed.update(status='4')
        finally:
            pass

    def patch_context(self):
        self.context['fields'] = self.fields

    def get_context_data(self, **kwargs):
        self.context = super().get_context_data(**kwargs)
        self.patch_context()
        self.update_failed()

        return self.context
