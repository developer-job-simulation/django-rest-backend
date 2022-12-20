from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view

from pokemon.models import Pokemon, VALID_POKEMON_TYPES
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
    try:
        pokemon = Pokemon.objects.get(id=id)
        serializer = PokemonSerializer(pokemon)
        return JsonResponse(serializer.data, safe=False, json_dumps_params={'ensure_ascii': False})
    except Pokemon.DoesNotExist:
        return JsonResponse({'error': 'Not found'}, status=404)


@csrf_exempt
@api_view(['GET'])
def pokemon_by_name(request, name):
    """
    Get Pokemon by name
    """
    try:
        pokemon = Pokemon.objects.get(name_english__iexact=name)
        serializer = PokemonSerializer(pokemon)
        return JsonResponse(serializer.data, safe=False, json_dumps_params={'ensure_ascii': False})
    except Pokemon.DoesNotExist:
        return JsonResponse({'error': 'Not found'}, status=404)


@csrf_exempt
def pokemon_by_type(request, pokemon_type):
    """
    Get Pokemon by type
    """
    pokemon = Pokemon.objects.filter(types__type__iexact=pokemon_type)
    if pokemon:
        serializer = PokemonSerializer(pokemon, many=True)
        return JsonResponse(serializer.data, safe=False, json_dumps_params={'ensure_ascii': False})
    else:
        return JsonResponse({'error': 'Bad request'}, status=404)


@csrf_exempt
def pokemon_by_hp(request):
    """
    Get Pokemon by HP
    """
    pokemon = Pokemon.objects.all()
    for k, v in request.GET.items():
        if k == 'lt':
            pokemon = pokemon.filter(hp__lt=v)
        elif k == 'lte':
            pokemon = pokemon.filter(hp__lte=v)
        elif k == 'gt':
            pokemon = pokemon.filter(hp__gt=v)
        elif k == 'gte':
            pokemon = pokemon.filter(hp__gte=v)
        else:
            return JsonResponse({'error': 'Invalid Operator. Must be one of ["gt","gte","lt","lte"]'},
                                status=404)
    if pokemon:
        serializer = PokemonSerializer(pokemon, many=True)
        return JsonResponse(serializer.data, safe=False, json_dumps_params={'ensure_ascii': False})
    else:
        return JsonResponse({'error': 'Not found'}, status=404)
