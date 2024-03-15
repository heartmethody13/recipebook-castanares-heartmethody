from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from ledger.models import Recipe, RecipeIngredient


def recipe_list(request):
    recipe_list = {'recipe_list': Recipe.objects.all()}

    return render(request, 'recipe_list.html', recipe_list)


@login_required
def recipe(request, pk):
    recipe_name = Recipe.objects.get(pk=pk)
    recipe_detail = { 
        'ingredients': RecipeIngredient.objects.filter(recipe__name=recipe_name), 
        'recipe': Recipe.objects.get(name=recipe_name),
    }

    return render(request, 'recipe_detail.html', recipe_detail)