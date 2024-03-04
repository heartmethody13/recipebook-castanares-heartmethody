from django.contrib import admin

from .models import Recipe, RecipeIngredient


class RecipeIngredientAdmin(admin.TabularInline):
    model = RecipeIngredient


class RecipeAdmin(admin.ModelAdmin):
    model = Recipe
    inlines = [RecipeIngredientAdmin]


admin.site.register(Recipe, RecipeAdmin)