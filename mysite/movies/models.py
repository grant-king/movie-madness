from django.db import models
from django.contrib.auth.models import User
import tmdbsimple as tmdb
import json

class Movie(models.Model):
    tmdb_id = models.IntegerField()
    title = models.CharField(max_length=100, default='')
    top_crew = models.CharField(max_length=400, default=['' for i in range(5)])
    top_cast = models.CharField(max_length=400, default=['' for i in range(5)])
    back_image = models.CharField(max_length=100, default='https://via.placeholder.com/150x350')
    poster_path = models.CharField(max_length=100, default='https://via.placeholder.com/150x350')
    featured_image = models.CharField(max_length=100, default='https://via.placeholder.com/350x150')
    content_image_1 = models.CharField(max_length=100, default='https://via.placeholder.com/350x150')
    content_image_2 = models.CharField(max_length=100, default='https://via.placeholder.com/350x150')
    tagline = models.CharField(max_length=100, default='')
    overview = models.TextField(default='')

    def __str__(self):
        return self.title

    def _tmdb_auth(self):
        # Load credentials from json file
        with open('movies/tmdb_credentials.json', "r") as file:
            creds = json.load(file)
        tmdb.API_KEY = creds['API_KEY']

    def _get_info(self, tmdb_id):
        self._tmdb_auth()
        movie = tmdb.Movies(tmdb_id)
        response = movie.info()

        response['top_crew'] = self._top_crew_list(movie)
        response['top_cast'] = self._top_cast_list(movie)
        response['back_image'] = self._single_url(movie.images()['posters'])
        response['featured_image'] = self._single_url(movie.images()['backdrops'])
        response['content_image_1'] = self._single_url(movie.images()['backdrops'])
        response['content_image_2'] = self._single_url(movie.images()['backdrops'])
        return response

    def _single_url(self, image_url_suffix_list):
        from random import choice
        url_list = []
        img_base_url = 'http://image.tmdb.org/t/p/original'

        for dictionary in image_url_suffix_list:
            url_list.append(img_base_url + dictionary['file_path'])

        return choice(url_list)

    def _top_cast_list(self, movie):
        jobs = [movie.credits()['cast'][i]['character'] for i in range(5)]
        people = [movie.credits()['cast'][i]['name'] for i in range(5)]
        return dict(zip(jobs, people))

    def _top_crew_list(self, movie):
        jobs = [movie.credits()['crew'][i]['job'] for i in range(5)]
        people = [movie.credits()['crew'][i]['name'] for i in range(5)]
        return dict(zip(jobs, people))

    @classmethod
    def create(cls, tmdb_id):
        id = int(tmdb_id)

        with open('movies/tmdb_credentials.json', "r") as file:
            creds = json.load(file)
        tmdb.API_KEY = creds['API_KEY']
        movie = tmdb.Movies(tmdb_id)
        response = movie.info()

        response['top_crew'] = Movie._top_crew_list(cls, movie)
        response['top_cast'] = Movie._top_cast_list(cls, movie)
        response['back_image'] = Movie._single_url(cls, movie.images()['posters'])
        response['featured_image'] = Movie._single_url(cls, movie.images()['backdrops'])
        response['content_image_1'] = Movie._single_url(cls, movie.images()['backdrops'])
        response['content_image_2'] = Movie._single_url(cls, movie.images()['backdrops'])
        info = response
        return cls(tmdb_id=id,
                   title=info['title'],
                   top_crew=info['top_crew'],
                   top_cast=info['top_cast'],
                   back_image=info['back_image'],
                   poster_path=info['poster_path'],
                   featured_image=info['featured_image'],
                   content_image_1=info['content_image_1'],
                   content_image_2=info['content_image_2'],
                   tagline=info['tagline'],
                   overview=info['overview'])

class Crew(models.Model):
    first = models.CharField(max_length=20)
    last = models.CharField(max_length=20)

class Actor(Crew):
    pass

class Director(Crew):
    pass

class Collection(models.Model):
    title = models.CharField(max_length=60)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, default='grant')

    def __str__(self):
        return self.title

class Category(models.Model):
    title = models.CharField(max_length=60)
    movie = models.ManyToManyField(Movie)
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)

    def __str__(self):
        return self.title