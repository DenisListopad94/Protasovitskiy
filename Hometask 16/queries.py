# При помощи “сырого” запроса вывести все фильмы, которые были сняты с 2015 по 2020 год.
all_movies = """
        SELECT name_movie FROM movies
        WHERE release BETWEEN 2015 and 2020
        """
# 2. Использую SQLite3 при помощи “сырого” запроса вывести актёров и режиссёров,
# которые не участвовали не в одном из фильмов.
not_movie_actors = """
        SELECT actors.name, actors.surname
        FROM actors
        LEFT JOIN actors_movies on actors_movies.actors_id == actors.actors_id
        LEFT JOIN movies on movies.movie_id == actors_movies.movies_id
        WHERE movies.name_movie is NULL
        """
not_movie_directors = """
        SELECT directors.name, directors.surname
        FROM directors
        LEFT JOIN movies ON directors.director_id == movies.director_id
        WHERE movies.name_movie is NULL
        """
# 3. Использую SQLite3 при помощи “сырого” запроса вывести все фильмы
# которые были сняты после 2000 года и в которых приняло участие более 1 актёра.
more_one_actor = """
       SELECT movies.name_movie, movies.release
        FROM movies
        INNER JOIN actors_movies on actors_movies.movies_id = movies.movie_id
        INNER JOIN actors on actors.actors_id = actors_movies.actors_id
        WHERE movies.release > 2000
        GROUP BY movies.name_movie
        HAVING COUNT(actors.surname) >= 2
        """
# 4. Использую SQLite3 при помощи “сырого” запроса вывести первых 5 самых высокооплачиваемых актёров.
high_paid_actors = """
        SELECT actors.name, actors.surname, movies.budjet
        FROM actors
        INNER JOIN actors_movies on actors_movies.actors_id = actors.actors_id
        INNER JOIN movies on movies.movie_id = actors_movies.movies_id
        WHERE movies.budjet >= 100000000
        LIMIT 5
        """
# 5. Использую SQLite3 при помощи “сырого” запроса вывести всех режиссёров и актёров
# которые были задействованы только в 1 фильме.
one_movie_actor = """
        SELECT actors.name, actors.surname
        FROM actors
        INNER JOIN actors_movies on actors_movies.actors_id = actors.actors_id
        INNER JOIN movies on movies.movie_id = actors_movies.movies_id
        GROUP BY actors.surname
        HAVING COUNT(movies.movie_id) = 1
        """
one_movie_director = """
        SELECT directors.name, directors.surname
        FROM directors
        INNER JOIN movies on directors.director_id = movies.director_id
        GROUP BY directors.surname
        HAVING COUNT(movies.movie_id) = 1
        """












