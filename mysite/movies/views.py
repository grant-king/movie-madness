from django.shortcuts import render
from .models import Movie, Collection, Category
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import path, reverse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


def home(request):
    return render(request, 'movies/home.html')

def example(request):
    return render(request, 'movies/example.html')

def collection(request):
    context = {'collection': Movie.objects.all()}
    return render(request, 'movies/category_list.html', context)

def item(request):
    from random import choice
    form = tmdb_id_form()
    context = {'movie': choice(Movie.objects.all()), 'form':form}
    return render(request, 'movies/item_base.html', context)

class CategoryListView(ListView):
    model = Category
    template_name = 'movies/category_list.html'
    context_object_name = 'objects'
    ordering = ['title']

class CategoryDetailView(DetailView):
    model = Category

class CategoryCreateView(LoginRequiredMixin, CreateView):
    model = Category
    fields = ['title', 'movie', 'collection']

class CategoryUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Category
    fields = ['title', 'movie', 'collection']

    def test_func(self):
        """check to see if user attempting to update category is owner"""
        category = self.get_object()
        if self.request.user == category.collection.owner:
            return True
        return False

class CategoryDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Category
    fields = ['title', 'movie', 'collection']

    def test_func(self):
        """check to see if user attempting to update category is owner"""
        category = self.get_object()
        if self.request.user == category.collection.owner:
            return True
        return False

    def get_success_url(self):
        return reverse('category-list')

class MovieListView(ListView):
    model = Movie
    template_name = 'movies/movie_list.html'
    context_object_name = 'objects'
    ordering = ['title']


class MovieDetailView(DetailView):
    model = Movie


class MovieCreateView(CreateView):
    model = Movie
    fields = ['tmdb_id']

    def get_success_url(self):
        return reverse('movie-list')

    def form_valid(self, form):
        form.instance = Movie.create(form.instance.tmdb_id)
        return super().form_valid(form)