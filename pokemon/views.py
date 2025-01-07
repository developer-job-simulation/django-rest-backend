from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from django.db.models import Q
import pokemon
from pokemon.models import Pokemon, VALID_POKEMON_TYPES, PokemonTypes
from pokemon.serializers import PokemonSerializer


@csrf_exempt
@api_view(['GET'])
def pokemon_list(request):
    """
    List all Pokemon
    """
    pokemon = Pokemon.objects.all()
    serializer = PokemonSerializer(pokemon, many=True)
    return JsonResponse(serializer.data, safe=False, json_dumps_params={'ensure_ascii': False})


@csrf_exempt
@api_view(['GET'])
def pokemon_by_id(request, id):
    """
    Get Pokemon by ID
    """
    pokemon = Pokemon.objects.get(id=id)
    serializer = PokemonSerializer(pokemon)
    return JsonResponse(serializer.data, safe=False, json_dumps_params={'ensure_ascii': False})


@csrf_exempt
@api_view(['GET'])
def pokemon_by_name(request, name):
    """
    Get Pokemon by name
    """
    pokemon = Pokemon.objects.filter(
            Q(name_english__icontains=name) |
            Q(name_japanese__icontains=name) |
            Q(name_chinese__icontains=name) |
            Q(name_french__icontains=name)
    )
    serializer = PokemonSerializer(pokemon, many=True)
    return JsonResponse(serializer.data, safe=False, json_dumps_params={'ensure_ascii': False})


@csrf_exempt
def pokemon_by_type(request, pokemon_type):
    """
    Get Pokemon by type
    """
    pokemon_types = PokemonTypes.objects.filter(type=pokemon_type)
    pokemons = [ pokemon_type.pokemon for pokemon_type in pokemon_types]
    serializer = PokemonSerializer(pokemons, many=True)
    return JsonResponse(serializer.data, safe=False, json_dumps_params={'ensure_ascii': False})

@csrf_exempt
def pokemon_by_hp(request):
    """
    Get Pokemon by HP
    """
    # TODO: Implement Endpoint
    return HttpResponse(status=501)
