from django.db import models


class Character(models.Model):
    name = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def get_name(self):
        return self.name