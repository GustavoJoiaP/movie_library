from typing import Dict

from domain.entities.actor import Actor
from domain.entities.director import Director
from domain.entities.movie import Movie
from domain.entities.producer import Producer
from domain.value_objects.person_genre import PersonGenre
from domain.value_objects.age import Age
from domain.value_objects.award_amount import AwardAmount
from domain.value_objects.movie_genre import MovieGenre
from domain.value_objects.name import Name


class MovieFactory:
    def build(self, data: Dict) -> Movie:
        # building actor
        actor_name = Name(data['actor']['first_name'], data['actor']['last_name'])
        actor_age = Age(data['actor']['age'])
        actor_award_amount = AwardAmount(data['actor']['award_amount'])
        actor_genre = PersonGenre(data['actor']['genre'])
        actor = Actor(actor_name, actor_age, actor_award_amount, actor_genre)

        # building director
        director_name = Name(data['director']['first_name'], data['director']['last_name'])
        director_age = Age(data['director']['age'])
        director_award_amount = AwardAmount(data['director']['award_amount'])
        director_genre = PersonGenre(data['director']['genre'])
        director = Director(director_name, director_age, director_award_amount, director_genre)

        # building producer
        producer_name = Name(data['producer']['first_name'], data['producer']['last_name'])
        producer_age = Age(data['producer']['age'])
        producer_award_amount = AwardAmount(data['producer']['award_amount'])
        producer = Producer(producer_name, producer_age, producer_award_amount)

        # building movie
        movie_title = data['title']
        movie_genre = MovieGenre(data['genre'])


        # returning movie
        movie = Movie(movie_title, movie_genre, actor, director, producer)
        return movie

        