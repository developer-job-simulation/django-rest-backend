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
    return JsonResponse(serializer.data, safe=False, json_dumps_params={'ensure_ascii': False, 'indent': 4})


@csrf_exempt
@api_view(['GET'])
def pokemon_by_id(request, id):
    try:
        pokemon = Pokemon.objects.get(id=id)
        serializer = PokemonSerializer(pokemon, many=False)
        return JsonResponse(serializer.data, safe=False, json_dumps_params={'ensure_ascii': False, 'indent': 4})
    except Pokemon.DoesNotExist:
        message = {'error': 'Not found'}
        return JsonResponse(message, status=404, json_dumps_params={'ensure_ascii': False, 'indent': 4})


@csrf_exempt
@api_view(['GET'])
def pokemon_by_name(request, name):
    # Make the first letter of the name uppercase and the rest lowercase
    name = name.capitalize()
    try:
        pokemon = Pokemon.objects.get(name_english=name)
        serializer = PokemonSerializer(pokemon, many=False)
        return JsonResponse(serializer.data, safe=False, json_dumps_params={'ensure_ascii': False, 'indent': 4})
    except Pokemon.DoesNotExist:
        message = {'error': 'Not found'}
        return JsonResponse(message, status=404, json_dumps_params={'ensure_ascii': False, 'indent': 4})

@csrf_exempt
def pokemon_by_type(request, pokemon_type):
    pokemon_type = pokemon_type.lower()  # Convert pokemon_type to lowercase
    VALID_POKEMON_TYPES = ['fire', 'water', 'grass', 'electric', 'psychic', 'ghost', 'dark', 'fairy', 'rock', 'ground', 'steel', 'flying', 'fighting', 'bug', 'ice', 'dragon', 'poison', 'normal']  # Add or modify this list based on your data

    if pokemon_type not in VALID_POKEMON_TYPES:
        return JsonResponse({'error': 'Bad request'}, status=400)

    try:
        pokemon = Pokemon.objects.filter(types__type__iexact=pokemon_type)
        # Check if Database returned nothing
        if pokemon.count() == 0:
            raise Pokemon.DoesNotExist
        serializer = PokemonSerializer(pokemon, many=True)
        return JsonResponse(serializer.data, safe=False, json_dumps_params={'ensure_ascii': False, 'indent': 4})
    except Pokemon.DoesNotExist:
        message = {'error': f'There are no Pokemon with type {pokemon_type}'}
        return JsonResponse(message, status=400)


@csrf_exempt
def pokemon_by_hp(request):
    """
    Get Pokemon by HP
    """
    hp_gt = request.GET.get('gt', None)  # Get the 'gt' parameter from the request, default value is None
    hp_lt = request.GET.get('lt', None)  # Get the 'lt' parameter from the request, default value is None

    if hp_gt is None and hp_lt is None:
        return JsonResponse({'error': 'Invalid Operator. Must be one of ["gt","gte","lt","lte"]'}, status=400)
    elif hp_gt is None :
        try:
            pokemon = Pokemon.objects.filter(hp__lte=hp_lt)  # Filter Pokemon with HP less than or equal to the specified value
            if pokemon.count() == 0:
                raise Pokemon.DoesNotExist
            serializer = PokemonSerializer(pokemon, many=True)
            return JsonResponse(serializer.data, safe=False, json_dumps_params={'ensure_ascii': False, 'indent': 4})
        except Pokemon.DoesNotExist:
            message = {'error': f'There are no Pokemon with HP less than or equal to {hp_lt}'}
            return JsonResponse(message, status=400)
    elif hp_lt is None:
        try:
            pokemon = Pokemon.objects.filter(hp__gte=hp_gt)  # Filter Pokemon with HP greater than or equal to the specified value
            if pokemon.count() == 0:
                raise Pokemon.DoesNotExist
            serializer = PokemonSerializer(pokemon, many=True)
            return JsonResponse(serializer.data, safe=False, json_dumps_params={'ensure_ascii': False, 'indent': 4})
        except Pokemon.DoesNotExist:
            message = {'error': f'There are no Pokemon with HP greater than or equal to {hp_gt}'}
            return JsonResponse(message, status=400)
    else:
        try:
            pokemon = Pokemon.objects.filter(hp__gte=hp_gt, hp__lte=hp_lt)  # Filter Pokemon with HP within the specified range
            if pokemon.count() == 0:
                raise Pokemon.DoesNotExist
            serializer = PokemonSerializer(pokemon, many=True)
            return JsonResponse(serializer.data, safe=False, json_dumps_params={'ensure_ascii': False, 'indent': 4})
        except Pokemon.DoesNotExist:
            message = {'error': f'There are no Pokemon with HP greater than or equal to {hp_gt} and less than or equal to {hp_lt}'}
            return JsonResponse(message, status=400)
    
