from django.shortcuts import render
from utils.recipes.factory import make_recipe
from home.models import Recipe

def home(request):
    recipes = Recipe.objects.filter(
        is_published=True
    ).order_by('-id')
    return render(request, 'home/pages/home.html', context = {
        'recipes': recipes,
    })

def category(request, category_id):
    recipes = Recipe.objects.filter(
        category__id=2,
        is_published=True
        ).order_by('-id')
    
    category_name = (
        getattr(recipes.first(), 'category', None),
        'name',
        'Not found'
    )

    return render(request, 'home/pages/category.html', context = {
        'recipes': recipes,
        'title': f'{category_name}'
    })

def recipe(request, id):
    return render(request, 'home/pages/recipe-view.html', context = {
        'recipe': make_recipe(),
        'is_detail_page': True,
    })

