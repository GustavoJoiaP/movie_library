from unittest import TestCase

from domain.entities.actor import Actor
from domain.entities.director import Director
from domain.entities.movie import Movie
from domain.entities.producer import Producer
from domain.value_objects.movie_genre import MovieGenre


class TestMovie(TestCase):
    def test_init_when_valid_args_then_build_movie(self):
        #Arrenge

        actor = Actor('Gustavo Joia', 23, 3, 'male')
        director = Director('Glauber Mestre', 31, 10, 'male')
        producer = Producer('Laboratorio Arquitetura', 20, 30)
        movie_title = 'CursoGlaubicho'
        movie_genre = MovieGenre('action')
        # data_dict_movie = (movie_title, movie_genre, actor, director, producer)
        # movie_factory = factory.build(data_dict_movie)

        #Action
        movie = Movie(movie_title, movie_genre, actor, director, producer)

        #Assert
        self.assertIsInstance(movie, Movie)
