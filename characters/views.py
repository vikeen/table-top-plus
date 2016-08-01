from django.views import generic
from django.core.urlresolvers import reverse_lazy

from .models import Character


class Index(generic.ListView):
    model = Character
    context_object_name = 'characters'


class Create(generic.CreateView):
    model = Character
    fields = ["name", "game_template"]


class Update(generic.UpdateView):
    model = Character
    fields = ["name", "game_template"]
    template_name = 'characters/character_form.html'


class Delete(generic.DeleteView):
    model = Character
    success_url = reverse_lazy('characters:index')
