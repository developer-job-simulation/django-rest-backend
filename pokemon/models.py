from django.db import models

VALID_POKEMON_TYPES = [("Bug", "Bug"), ("Dark", "Dark"), ("Dragon", "Dragon"), ("Electric", "Electric"), ("Fairy", "Fairy"),
                       ("Fighting", "Fighting"), ("Fire", "Fire"), ("Flying", "Flying"), ("Ghost", "Ghost"),
                       ("Grass", "Grass"), ("Ground", "Ground"), ("Ice", "Ice"), ("Normal", "Normal"), ("Poison", "Poison"),
                       ("Psychic", "Psychic"), ("Rock", "Rock"), ("Steel", "Steel"), ("Water", "Water")]


class Pokemon(models.Model):
    id = models.IntegerField(primary_key=True)
    name_english = models.TextField(blank=False, null=False, default="")
    name_japanese = models.TextField(blank=False, null=False, default="")
    name_chinese = models.TextField(blank=False, null=False, default="")
    name_french = models.TextField(blank=False, null=False, default="")
    hp = models.IntegerField(blank=False, null=False, default=0)
    attack = models.IntegerField(blank=False, null=False, default=0)
    defense = models.IntegerField(blank=False, null=False, default=0)
    special_attack = models.IntegerField(blank=False, null=False, default=0)
    special_defense = models.IntegerField(blank=False, null=False, default=0)
    speed = models.IntegerField(blank=False, null=False, default=0)

    class Meta:
        db_table = "pokemon"


class PokemonTypes(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE, related_name="types", db_column="pokemon_id")
    type = models.TextField(choices=VALID_POKEMON_TYPES, blank=False, null=False, default="Normal")

    class Meta:
        db_table = "pokemon_types"
        unique_together = ('pokemon', 'type')
