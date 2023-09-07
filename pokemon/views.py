from django.http import Http404, JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from django.db.models import Q

from pokemon.models import Pokemon, VALID_POKEMON_TYPES
from pokemon.serializers import PokemonSerializer


@csrf_exempt
@api_view(["GET"])
def pokemon_list(request):
    """
    List all Pokemon
    """
    pokemon = Pokemon.objects.all()
    serializer = PokemonSerializer(pokemon, many=True)
    return JsonResponse(
        serializer.data, safe=False, json_dumps_params={"ensure_ascii": False}
    )


@csrf_exempt
@api_view(["GET"])
def pokemon_by_id(request, id):
    """
    Get Pokemon by ID
    """
    try:
        pokemon = get_object_or_404(Pokemon, id=id)
        serializer = PokemonSerializer(pokemon)
        return JsonResponse(serializer.data, safe=False)
    except Http404:
        return JsonResponse({"error": "Not found"}, status=404)


@csrf_exempt
@api_view(["GET"])
def pokemon_by_name(request, name):
    """
    Get Pokemon by name
    """
    try:
        pokemon = get_object_or_404(Pokemon, name_english__iexact=name)
        serializer = PokemonSerializer(pokemon)
        return JsonResponse(serializer.data, safe=False)
    except Http404:
        return JsonResponse({"error": "Not found"}, status=404)


@csrf_exempt
def pokemon_by_type(request, pokemon_type):
    """
    Get Pokemon by type
    """
    try:
        # check if type exists
        if pokemon_type.lower() not in [t[0].lower() for t in VALID_POKEMON_TYPES]:
            return JsonResponse({"error": "Bad request"}, status=400)

        pokemon = Pokemon.objects.filter(types__type__iexact=pokemon_type)
        serializer = PokemonSerializer(pokemon, many=True)
        return JsonResponse(serializer.data, safe=False)
    except Http404:
        return JsonResponse({"error": "Not found"}, status=404)


@csrf_exempt
def pokemon_by_hp(request):
    """
    Get Pokemon by HP
    """

    VALID_COMPARATORS = ["gt", "gte", "lt", "lte"]

    try:
        comparators = [
            comparator
            for comparator in VALID_COMPARATORS
            if request.GET.get(comparator)
        ]

        if not comparators:
            return JsonResponse(
                {"error": 'Invalid Operator. Must be one of ["gt","gte","lt","lte"]'},
                status=400,
            )

        # Initialize the filter with Q objects based on the selected comparators
        filter_query = Q()
        for comparator in comparators:
            value = int(request.GET.get(comparator))
            if comparator == "gt":
                filter_query &= Q(hp__gt=value)
            elif comparator == "gte":
                filter_query &= Q(hp__gte=value)
            elif comparator == "lt":
                filter_query &= Q(hp__lt=value)
            elif comparator == "lte":
                filter_query &= Q(hp__lte=value)

        pokemons = Pokemon.objects.filter(filter_query)
        serializer = PokemonSerializer(pokemons, many=True)

        if pokemons.exists():
            return JsonResponse(serializer.data, safe=False)
        else:
            return JsonResponse({"error": "Not found"}, status=404)

    except Http404:
        return JsonResponse({"error": "Not found"}, status=404)
