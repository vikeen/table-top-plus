from django.core.urlresolvers import reverse
from django.db import models


class Character(models.Model):
    GAME_TEMPLATE_CHOICES = (
        ('dnd_5e', 'Dungeons and Dragons 5th Edition'),
    )

    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    game_template = models.CharField(max_length=200, choices=GAME_TEMPLATE_CHOICES)

    def get_absolute_url(self):
        return reverse('characters:update', kwargs={'pk': self.pk})
