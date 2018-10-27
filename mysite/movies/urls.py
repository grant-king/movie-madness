from django.urls import path
from .views import CollectionListView, CategoryDetailView, MovieCreateView, CategoryCreateView
from . import views

urlpatterns = [
    path('', views.home, name='movies-home'),
    path('movie/', views.item, name='movies-item' ),
    path('example/', views.example, name='movies-example'),
    path('collection/', CollectionListView.as_view(), name='collection-list'),
    path('category/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
    path('category/new/', views.CategoryCreateView.as_view(), name='category-new'),
    path('movie/<int:pk>/', views.MovieDetailView.as_view(), name='movie-detail'),
    path('movie/new/', views.MovieCreateView.as_view(), name='movie-new')
]