from django.conf import settings
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from .models import Ingredient, Image
from userapp.models import ViewHistory
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


def index_view(request):
    ingredients = Ingredient.objects.all()
    return render(request, 'mainapp/ingredient_list.html', {'ingredients': ingredients})

def ingredient_search_view(request):
    search_query = request.GET.get('search')
    ingredients = Ingredient.objects.filter(name__icontains=search_query)
    return render(request, 'mainapp/ingredient_search.html', {'ingredients': ingredients})

class HomeView(TemplateView):
    template_name = 'mainapp/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        images = Image.objects.all()
        context['images'] = images
        return context


class IngredientListView(ListView):
    model = Ingredient
    template_name = 'mainapp/ingredient_list.html'
    context_object_name = 'ingredients'
    ordering = ['name']  # Сортировка по имени


class IngredientDetailView(DetailView):
    model = Ingredient
    template_name = 'mainapp/ingredient_detail.html'
    context_object_name = 'ingredient'

    @method_decorator(login_required)  # Requires the user to be logged in
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        ingredient = self.object

        # Create a new ViewHistory record for the current user and viewed ingredient
        ViewHistory.objects.create(user=self.request.user, viewed_item=str(ingredient))

        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        ingredient = self.object

        # Retrieve related sources for the ingredient
        sources = ingredient.sources.all()

        context['sources'] = sources
        return context