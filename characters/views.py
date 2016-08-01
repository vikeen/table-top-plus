from django.views import generic
from django.core.urlresolvers import reverse_lazy

from .models import Character


class index(generic.ListView):
    model = Character
    context_object_name = 'characters'


class create(generic.CreateView):
    model = Character
    fields = ["name"]


class detail(generic.DetailView):
    model = Character


class delete(generic.DeleteView):
    model = Character
    success_url = reverse_lazy('characters:index')
