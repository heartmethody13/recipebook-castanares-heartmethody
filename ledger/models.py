from django.db import models
from django.urls import reverse


class Ingredient(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name


class Recipe(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.name


    def get_absolute_url(self):
        return reverse('ledger:recipe-detail', args=[self.pk])
    

    def get_ingredients(self):
        Ingredient.objects.filter(recipe__recipe__name = self.name)


class RecipeField(models.Model):
    quantity = models.CharField(max_length=100)
    ingredient = models.ForeignKey(
        'Ingredient',
        on_delete=models.CASCADE,
        related_name='recipe'
    )
    recipe = models.ForeignKey(
        'Recipe',
        on_delete=models.CASCADE,
        related_name='ingredients'
    )