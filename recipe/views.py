from django.shortcuts import render, redirect, get_object_or_404
from .models import Recipe
from .forms import RecipeForm
from django.utils.text import slugify
from category.models import Category
from django.core.paginator import Paginator

def submit_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.submitter = request.user
            
            # Ensure the slug is unique
            slug = slugify(recipe.recipe_name)
            unique_slug = slug
            counter = 1
            while Recipe.objects.filter(slug=unique_slug).exists():
                unique_slug = '{}-{}'.format(slug, counter)
                counter += 1
            recipe.slug = unique_slug
            
            recipe.save()
            return redirect('show_recipe')
    else:
        form = RecipeForm()
    return render(request, 'submit_recipe.html', {'form': form})


def show_recipe(request, category_slug=None):
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        recipes = Recipe.objects.filter(category=category)
        
    else:
        if request.method == 'POST':
            need = request.POST['search_query']
            recipes =  Recipe.objects.filter(recipe_name__contains=need)
        else:
            recipes = Recipe.objects.all()
    

    paginator = Paginator(recipes, 4)
    page_number = request.GET.get('page')
    paged_recipes = paginator.get_page(page_number)

    categories = Category.objects.all()
    context = {'recipes': paged_recipes, 'categories': categories}
    return render(request, 'recipe.html', context)






def recipe_detail(request, id):
    single_recipe = Recipe.objects.get(pk = id)
    return render(request, 'recipe_detail.html', {'recipe': single_recipe})






