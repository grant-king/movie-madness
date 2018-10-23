from django.urls import path
from .views import CollectionListView, CategoryDetailView
from . import views

urlpatterns = [
    path('', views.home, name='movies-home'),
    path('item/', views.item, name='movies-item' ),
    path('example/', views.example, name='movies-example'),
    path('collection/', CollectionListView.as_view(), name='collection-list'),
    path('category/<int:pk>/', CategoryDetailView.as_view(), name='category-detail'),
]