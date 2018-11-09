# Movie Madness
Django demo movie collection app

Categorical gallery preview:
![alt text](https://raw.githubusercontent.com/grant-king/movie-madness/6624043c66882c8aa0bc78a234b2a59e503ceb96/mysite/screenshot_categories_gallery.jpg "category list view")

### Getting Started

##### Setup prerequisites
Get your tmdb api key

Clone the code.

Set up a new python 3 virtual environment and pip install:

* django

* django-crispy-forms

* tmdbsimple

* pillow

##### Start Server
Navigate your terminal to the directory containing cloned code on your local machine.

Something like:

 ` cd user/Documents/GitHub/movie-madness/mysite `

 Then start a webserver using manage.py:

 ` python manage.py runserver `

 Open a browser to the specified url to explore the app.

Before being able to load in movie details, you will have to insert your tmdb api key at the appropriate spot in the ` _tmdb_auth ` method of Movie object in models.py

Sign up for an account (details don't matter; this is just for )
