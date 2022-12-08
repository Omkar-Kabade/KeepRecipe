from django.urls import path
from . import views

urlpatterns = [
    path("",views.IndexRecipeList.as_view(), name = 'index-page'),
    path("all-recipes",views.AllRecipeList.as_view(), name="all-recipes"),
    path("recipe-details/<slug:slug>",views.RecipeDetailView.as_view(), name = 'recipe-details'),
    path("pinned-recipes",views.PinRecipe.as_view() ,name="pinned-recipes")
]
