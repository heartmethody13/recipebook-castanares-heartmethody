from django.urls import path
from .views import index, recipe_list, first_recipe, second_recipe


urlpatterns = [
    path('recipes/list', recipe_list, name = '/recipes/list'),
    path('recipe/1', first_recipe, name = '/recipe/1'),
    path('recipe/2', second_recipe, name = '/recipe/2')
]

app_name = "ledger"