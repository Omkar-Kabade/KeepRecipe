from django.shortcuts import render
from .models import Recipe
from django.db.models import Avg
from django.views.generic import ListView, DetailView,View
from django.urls import reverse
from .forms import CommentForm
from django.http import HttpResponseRedirect
# Create your views here.

class IndexRecipeList(ListView):
    template_name = "recipes/index.html"
    model = Recipe
    ordering = ["-rating"]
    context_object_name = "recipes"

    def get_queryset(self):
        query =  super().get_queryset()
        data = query[:3]
        return data
    
    def get_context_data(self, **kwargs):
        all_recipe = Recipe.objects.all()
        context =  super().get_context_data(**kwargs)
        context["total_recipe"] = all_recipe.count()
        context["avg_rating"] = all_recipe.aggregate(Avg("rating"))
        return context

class AllRecipeList(ListView):
    template_name = "recipes/all-recipes.html"
    model = Recipe
    ordering = ["-rating"]
    context_object_name = "recipes"
        
class RecipeDetailView(View):

    def pinned_recipe(self,request,recipe_id):
        pinned_recipes = request.session.get("pinned_recipes")
        if pinned_recipes is not None:
            pinned = recipe_id in pinned_recipes
        else:
            pinned= False
        return pinned

    def get(self, request, slug):
        recipe = Recipe.objects.get(slug = slug)
        context = {
            "recipe":recipe,
            "tags":recipe.tags.all(),
            "commentForm":CommentForm(),
            "comments":recipe.comments.all().order_by("-id"),
            "pinned":self.pinned_recipe(request,recipe.id)
        }
        return render (request, "recipes/recipe-details.html",context)
    
    def post(self, request, slug):
        form = CommentForm(request.POST)
        recipe = Recipe.objects.get(slug = slug)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.recipe = recipe
            comment.save()
            return HttpResponseRedirect(reverse("recipe-details",args = [slug])) # this redirect will come as get

         
        context = {
            "recipe":recipe,
            "tags":recipe.tags.all(),
            "commentForm":form,
            "comments":recipe.comments.all().order_by("-id"),
            "pinned":self.pinned_recipe(request,recipe.id)
        }

        return render(request,"recipes/recipe-details.html",context) # this will be as post when any error has occured


class PinRecipe(View):
    def get(self, request):
        pinned_recipes = request.session.get("pinned_recipes")
        context = {}
        if pinned_recipes is None or len(pinned_recipes) == 0:
            context["has_pins"] = False
            context["pinned_recipe"] = []
        else:
            recipe = Recipe.objects.filter(id__in = pinned_recipes) # it check whethr how many recipe from model are in session list
            context["pinned_recipe"] = recipe
            context["has_pins"] = True
        return render(request, "recipes/pinned-recipes.html", context)

    def post(self, request):
        pinned_recipes = request.session.get("pinned_recipes") #to check 

        if pinned_recipes is None:
            pinned_recipes = []
        
        recipe_id = int(request.POST["recipe_id"]) #it is always in string

        if recipe_id not in pinned_recipes:
            pinned_recipes.append(recipe_id) #pins the recipe
        else:
            pinned_recipes.remove(recipe_id) #unpins the recipe

        request.session["pinned_recipes"] = pinned_recipes # to save the above data in session 

        return HttpResponseRedirect("/")
        




