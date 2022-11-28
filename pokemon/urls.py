from django.urls import path
from pokemon import views

urlpatterns = [
    path('pokemon/', views.pokemon_list),
    path('pokemon/<int:id>/', views.pokemon_by_id),
    path('pokemon/name/<str:name>/', views.pokemon_by_name),
    path('pokemon/type/<str:pokemon_type>/', views.pokemon_by_type),
    path('pokemon/hp/', views.pokemon_by_hp),
]