from django.views import generic

from .models import Character


class IndexView(generic.ListView):
    template_name = 'characters/index.html'
    context_object_name = 'characters'

    def get_queryset(self):
        return [{
            'id': 1,
            'name': 'Macu'
        },
            {
                'id': 2,
                'name': 'Vikeen'
            }]


class DetailView(generic.DetailView):
    model = Character
    template_name = 'characters/detail.html'
