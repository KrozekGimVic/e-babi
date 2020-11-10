from django.shortcuts import render

from recepti.models import Recipe


def homepage(request):
    last5 = Recipe.objects.order_by('-id')[:5]
    return render(request, 'recepti/homepage.html', {
        'latest': last5,
    })
