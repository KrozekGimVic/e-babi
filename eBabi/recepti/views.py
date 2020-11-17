from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, CreateView

from recepti.models import Recipe
from recepti.forms import CompareForm

def homepage(request):
    last5 = Recipe.objects.order_by('-id')[:5]
    return render(request, 'recepti/homepage.html', {
        'latest': last5,
    })

class RecipeDetailView(DetailView):
    model = Recipe

class RecipeCreateView(CreateView):
    model = Recipe
    fields = ['title', 'content', 'preparation_time']


def compare(request):
    if request.GET:
        form = CompareForm(request.GET)
        if form.is_valid():
            return render(request, 'recepti/compare_results.html', {
                'r1': form.cleaned_data['r1'],
                'r2': form.cleaned_data['r2'],
            })
    else:
        form = CompareForm()
    return render(request, 'recepti/compare.html', {
        'form': form,
    })
