from django.urls import path

from .views import recipe, recipe_list

urlpatterns = [
    path('recipes/list', recipe_list, name = 'list'),
    path('recipe/<int:pk>', recipe, name = 'recipe-detail'),
]

app_name = "ledger"