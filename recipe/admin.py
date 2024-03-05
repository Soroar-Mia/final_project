from django.contrib import admin
from . models import Recipe

class RecipeAdmin(admin.ModelAdmin): 
     list_display = ['id', 'recipe_name', 'description', 'image', 'category']
     
     prepopulated_fields = {'slug' : ('recipe_name',)}
     
admin.site.register(Recipe, RecipeAdmin)
