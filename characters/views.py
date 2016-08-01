from django.views import generic
from django.core.urlresolvers import reverse_lazy

from .models import Character


class Index(generic.ListView):
    model = Character
    context_object_name = 'characters'


class Create(generic.CreateView):
    model = Character
    fields = ["name"]


class Detail(generic.DetailView):
    model = Character


class Delete(generic.DeleteView):
    model = Character
    success_url = reverse_lazy('characters:index')
