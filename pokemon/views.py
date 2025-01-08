from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from django.db.models import Q
from pokemon.models import Pokemon, PokemonTypes
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
    pokemon_types = PokemonTypes.objects.filter(type__icontains=pokemon_type)
    pokemons = [ pokemon_type.pokemon for pokemon_type in pokemon_types]
    if pokemons == []:
        return JsonResponse({"error":"Bad request"})
    serializer = PokemonSerializer(pokemons, many=True)
    return JsonResponse(serializer.data, safe=False, json_dumps_params={'ensure_ascii': False})

@csrf_exempt
def pokemon_by_hp(request):
    """
    Get Pokemon by HP
    """
    params = request.GET
    hp_lt = request.GET.get("lt")
    hp_gt = request.GET.get("gt")
    query = Q()

    for key in params:
        if key not in ["gt","gte","lt","lte"]:
            return JsonResponse({"error":'Invalid Operator. Must be one of ["gt","gte","lt","lte"]'})

    if hp_gt:
        query &= Q(hp__gt = hp_gt)

    if hp_lt:
        query &= Q(hp__lt = hp_lt)

    if hp_gt and hp_lt:
        if hp_gt > hp_lt:
            return JsonResponse({"error":"Not found"},status=404)

    pokemons = Pokemon.objects.filter(query)
    serializer = PokemonSerializer(pokemons,many=True)

    return JsonResponse(serializer.data, safe=False, json_dumps_params={'ensure_ascii': False})

