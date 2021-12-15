from array import array

from domain.entities.actor import Actor
from domain.entities.director import Director
from domain.entities.producer import Producer
from domain.value_objects.movie_genre import MovieGenre


class Movie:
    title: str
    genre: MovieGenre
    actor: list[Actor]
    director: list[Director]
    producer: list[Producer]

    def __init__(self, title: str, genre: MovieGenre, actor: Actor, director: Director, producer: Producer):
        self.title = title
        self.genre = genre
        self.actor = actor
        self.director = director
        self.producer = producer