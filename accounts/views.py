from django.shortcuts import render
from django.views.generic import FormView
from .forms import UserRegistrationForm,UserUpdateForm
from django.contrib.auth import login
from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView
from django.views import View
from django.shortcuts import redirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from recipe.models import Recipe
from recipe.models import Category



class UserRegistrationView(FormView):
    template_name = 'accounts/user_registration.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('profile')
    
    def form_valid(self,form):
        print(form.cleaned_data)
        user = form.save()
        login(self.request, user)
        print(user)
        return super().form_valid(form) 
    
class UserLoginView(LoginView):
    template_name = 'accounts/user_login.html'
    def get_success_url(self):
        return reverse_lazy('show_recipe')

 
@login_required
def logout_view(request):
    logout(request)
    # Redirect to a specific page after logout
    return redirect('home')  # Replace 'home' with the name of your home URL pattern



class UserBankAccountUpdateView(View):
    template_name = 'accounts/profile.html'

    def get(self, request):
        form = UserUpdateForm(instance=request.user)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')  
        return render(request, self.template_name, {'form': form})
    
# def show_recipe_p(request, category_slug=None):
#     if category_slug:
#         category = get_object_or_404(Category, slug=category_slug)
#         recipes = Recipe.objects.filter(category=category)
#     else:
#         recipes = Recipe.objects.all()

#     paginator = Paginator(recipes, 4)
#     page_number = request.GET.get('page')
#     paged_recipes = paginator.get_page(page_number)

#     categories = Category.objects.all()
#     context = {'recipes': paged_recipes, 'categories': categories}
#     return render(request, 'recipe.html', context)

