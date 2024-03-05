from django.db import models

from category.models import Category
# Create your models here.

class Recipe(models.Model):
    id= models.IntegerField(primary_key=True)
    recipe_name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.TextField(max_length=500, blank=True)
    image = models.ImageField(upload_to='photos')
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.recipe_name
    
