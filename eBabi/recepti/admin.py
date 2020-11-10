from django.contrib import admin

from .models import Recipe, RecipeIngredient, Ingredient, Unit

admin.site.register(Recipe)
admin.site.register(RecipeIngredient)
admin.site.register(Ingredient)
admin.site.register(Unit)
