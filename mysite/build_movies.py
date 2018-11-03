from movies.models import Movie

refs = [754, 1701, 9679 , 1571, 4413, 16871, 19404, 637, 497, 680, 539, 13, 510, 599, 429, 452522]
for item in refs:
    Movie.create(item).save()

