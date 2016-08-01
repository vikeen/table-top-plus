from django.views import generic

from .models import Character


class IndexView(generic.ListView):
    model = Character
    template_name = 'characters/index.html'
    context_object_name = 'characters'


class CreateView(generic.CreateView):
    model = Character
    fields = ["name"]
    template_name = 'characters/create.html'


class DetailView(generic.DetailView):
    model = Character
    template_name = 'characters/detail.html'

