from django.urls import path
from . import views

urlpatterns = [
    path('submit/', views.submit_recipe, name='submit_recipe'),
    path('', views.show_recipe, name='show_recipe'),
    path('category/<slug:category_slug>/', views.show_recipe, name='category_by_slug'),# Corrected the URL name here
    path('recipe_detail/<int:id>', views.recipe_detail, name='recipe_detail'),
    # path('<slug:category_slug>/<slug:recipe_slug>/', views.recipe_detail, name='recipe_detail'),
]