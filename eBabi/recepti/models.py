from django.conf import settings
from django.db import models


class Ingredient(models.Model):
    name = models.CharField(max_length=50, help_text='Vpišite sestavino z malimi črkami v imenovalniku ednine.')

    def __str__(self):
        return self.name


class Recipe(models.Model):
    title = models.CharField(max_length=200, help_text="Naslov recepta.")
    content = models.TextField(max_length=60000, help_text="Vsebina recepta.")
    preparation_time = models.DurationField(help_text="Čas priprave [[hh:]mm:]ss")
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    ingredients = models.ManyToManyField(Ingredient, through='RecipeIngredient')

    def __str__(self):
        return self.title


class Unit(models.Model):
    NUMBER = 'N'
    LENGTH = 'L'
    TEMPERATURE = 'T'
    VOLUME = 'V'
    MASS = 'M'
    DIMENSIONS = (
        (NUMBER, 'število'),
        (LENGTH, 'dolžina'),
        (TEMPERATURE, 'temperatura'),
        (VOLUME, 'volumen'),
        (MASS, 'masa'),
    )

    name = models.CharField(max_length=50, unique=True)
    label = models.CharField(max_length=5)
    dimension = models.CharField(max_length=1, choices=DIMENSIONS)

    def __str__(self):
        return f'{self.name} ({self.dimension})'


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='ingredient_list')
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.FloatField()
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.recipe}: {self.ingredient} ({self.quantity} {self.unit.label})'
