from django.shortcuts import render
import tmdbsimple as tmdb
from .models import Movie, Collection, Category
from django.views.generic import ListView, DetailView, CreateView

def collection_movie_objects():
    refs = [4413, 1992, 590]
    collection = {}

    for index, item in enumerate(refs):
        var_str = 'Movie_' + str(index)
        collection[var_str] = Movie.create(item)

    return collection

def tmdb_id_form():
    from django import forms

def home(request):
    return render(request, 'movies/home.html')

class CollectionListView(ListView):
    model = Category
    template_name = 'movies/collection.html'
    context_object_name = 'objects'
    ordering = ['title']

def example(request):
    return render(request, 'movies/example.html')

def collection(request):
    context = {'collection': Movie.objects.all()}
    return render(request, 'movies/collection.html', context)

def item(request):
    from random import choice
    form = tmdb_id_form()
    context = {'movie': choice(Movie.objects.all()), 'form':form}
    return render(request, 'movies/item_base.html', context)


class CategoryDetailView(DetailView):
    model = Category


class CategoryCreateView(CreateView):
    model = Category
    fields = ['title']


class MovieDetailView(DetailView):
    model = Movie


class MovieCreateView(CreateView):
    model = Movie
    fields = ['tmdb_id']

    def form_valid(self, form):
        form.instance = Movie.create(form.instance.tmdb_id)
        return super().form_valid(form)