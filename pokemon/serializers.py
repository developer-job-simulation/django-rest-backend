from rest_framework import serializers
from pokemon.models import Pokemon, PokemonTypes


# TODO: Add a serializer for PokemonTypes, and use it as a nested serializer for PokemonSerializer

class PokemonTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PokemonTypes
        fields = ('type',)


class PokemonSerializer(serializers.ModelSerializer):
    types = PokemonTypeSerializer(many=True)

    class Meta:
        model = Pokemon
        fields = ('id', 'name_english', 'name_japanese', 'name_chinese', 'name_french', 'hp', 'attack', 'defense',
                  'special_attack', 'special_defense', 'speed', 'types',)
