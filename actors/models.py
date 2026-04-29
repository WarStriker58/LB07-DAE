from django.db import models

class Actor(models.Model):  # NUEVO
    name = models.CharField(max_length=150)
    birth_year = models.PositiveIntegerField()

    def __str__(self):
        return self.name