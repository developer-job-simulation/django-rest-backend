from django.contrib import admin
from .models import Pokemon, PokemonTypes

# Register your models here.
admin.site.register(Pokemon)
admin.site.register(PokemonTypes)
