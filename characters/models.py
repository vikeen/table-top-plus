from django.core.urlresolvers import reverse
from django.db import models


class Character(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def get_name(self):
        return self.name

    def get_absolute_url(self):
        return reverse('characters:detail', kwargs={'pk': self.pk})