from django.urls import path

from .views import recipe_list, recipe


urlpatterns = [
    path('recipes/list', recipe_list, name = 'list'),
    path('recipe/<int:pk>', recipe, name = 'recipe-detail'),
]

app_name = "ledger"