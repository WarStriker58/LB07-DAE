from django.contrib import admin
from .models import Actor

@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):  # NUEVO
    list_display = ('id', 'name', 'birth_year')
    search_fields = ('name',)