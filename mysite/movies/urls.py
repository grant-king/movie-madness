from django.urls import path
from .views import CategoryDetailView, MovieCreateView, CategoryCreateView, CategoryListView, MovieListView, CategoryDeleteView, CategoryUpdateView
from . import views

urlpatterns = [
    path('', views.home, name='movies-home'),
    path('movie/', views.item, name='movies-item' ),
    path('example/', views.example, name='movies-example'),
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('category/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
    path('category/new/', views.CategoryCreateView.as_view(), name='category-new'),
    path('category/<int:pk>/update/', views.CategoryUpdateView.as_view(), name='category-update'),
    path('category/<int:pk>/delete/', views.CategoryDeleteView.as_view(), name='category-delete'),
    path('movies/', views.MovieListView.as_view(), name='movie-list'),
    path('movie/<int:pk>/', views.MovieDetailView.as_view(), name='movie-detail'),
    path('movie/new/', views.MovieCreateView.as_view(), name='movie-new'),
]