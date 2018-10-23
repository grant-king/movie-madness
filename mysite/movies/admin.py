from django.contrib import admin
from .models import Movie, Collection, Category

admin.site.register(Movie)
admin.site.register(Collection)
admin.site.register(Category)