from django.urls import path

from . import views

urlpatterns = [
    path('', views.homepage, name='index'),
    path('recipe/<int:pk>/', views.RecipeDetailView.as_view(), name='recipe-detail'),
    path('recipe/-/create/', views.RecipeCreateView.as_view(), name='recipe-create'),
    path('compare/', views.compare, name='recipe-compare'),
]
