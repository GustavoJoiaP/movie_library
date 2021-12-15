from unittest import TestCase

from domain.entities.movie import Movie
from domain.factories.movie_factory import MovieFactory
from domain.value_objects.movie_genre import MovieGenre
from domain.value_objects.person_genre import PersonGenre


class TestMovieFactory(TestCase):
    def test_init_when_valid_args_then_build_movie(self):
        #Arrange
        factory = MovieFactory()

        data_dict_movie = {'title': 'CursoGlaubito', 'genre': MovieGenre.ACTION.value,
                           'actor': {'first_name': 'Gustavo', 'last_name': 'Paziani', 'age': 23,
                                     'award_amount': 3, 'genre': PersonGenre.MALE.value},
                           'director': {'first_name': 'Glaubito','last_name': 'Azevedo', 'age': 31,
                                        'award_amount': 15, 'genre': PersonGenre.MALE.value},
                           'producer': {'first_name': 'Laboratorio', 'last_name': 'Computer', 'age': 20,'award_amount': 60}}
        #Action
        movie = factory.build(data_dict_movie)

        #Assert
        self.assertIsInstance(movie, Movie)
