from django.contrib import admin

from .models import Ingredient, Recipe, RecipeField


class RecipeIngredient(admin.TabularInline):
    model = RecipeField


class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    inlines = [RecipeIngredient]


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient)
