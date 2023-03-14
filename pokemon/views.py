from django.http import JsonResponse
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
        pokemon = Pokemon.objects.get(pk=id)
        serializer = PokemonSerializer(pokemon)
        return JsonResponse(serializer.data, safe=False, json_dumps_params={'ensure_ascii': False})
    except Exception as e:
        return JsonResponse({'error': 'Not found'}, status=404)


@csrf_exempt
@api_view(['GET'])
def pokemon_by_name(request, name):
    """
    Get Pokemon by name
    """
    pokemon = Pokemon.objects.filter(name_english__iexact=name)
    if len(pokemon) == 0:
        return JsonResponse({'error': 'Not found'}, status=404)
    serializer = PokemonSerializer(pokemon.first())
    return JsonResponse(serializer.data, safe=False, json_dumps_params={'ensure_ascii': False})


@csrf_exempt
def pokemon_by_type(request, pokemon_type):
    """
    Get Pokemon by type
    """
    pokemon_type = pokemon_type.lower().capitalize()
    if VALID_POKEMON_TYPES.count((pokemon_type, pokemon_type)) == 0:
        return JsonResponse({'error': 'Bad request'}, status=400)
    pokemon = Pokemon.objects.filter(types__type__iexact=pokemon_type)
    if len(pokemon) == 0:
        return JsonResponse({'error': 'Not found'}, status=404)
    serializer = PokemonSerializer(pokemon, many=True)
    return JsonResponse(serializer.data, safe=False, json_dumps_params={'ensure_ascii': False})


@csrf_exempt
def pokemon_by_hp(request):
    """
    Get Pokemon by HP
    """
    pokemon = Pokemon.objects.all()
    lt = request.GET.get('lt')
    gt = request.GET.get('gt')
    lte = request.GET.get('lte')
    gte = request.GET.get('gte')

    valid_query_params = set(['lt', 'gt', 'lte', 'gte'])

    if not set(request.GET.keys()) <= valid_query_params:
        return JsonResponse({'error': 'Invalid Operator. Must be one of ["gt","gte","lt","lte"]'}, status=400)

    if lt is not None:
        pokemon = pokemon.filter(hp__lt=int(lt))
    if gt is not None:
        pokemon = pokemon.filter(hp__gt=int(gt))
    if gte is not None:
        pokemon = pokemon.filter(hp__gte=int(gte))
    if lte is not None:
        pokemon = pokemon.filter(hp__lte=int(lte))

    if len(pokemon) == 0:
        return JsonResponse({'error': 'Not found'}, status=404)

    serializer = PokemonSerializer(pokemon, many=True)
    return JsonResponse(serializer.data, safe=False, json_dumps_params={'ensure_ascii': False})
