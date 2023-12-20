from typing import List

from config.database import Session
from models.movie import Movie as MovieModel
from schemas.movie import Movie


class MovieService:
    def __init__(self) -> None:
        self.db = Session()

    def get_movies(self) -> List[Movie]:
        result = self.db.query(MovieModel).all()
        return result

    def get_movie(self, id: int) -> Movie | None:
        result = self.db.query(MovieModel).filter(MovieModel.id == id).first()
        return result

    def get_movies_by_category(self, category: str) -> List[Movie]:
        result = self.db.query(MovieModel).filter(MovieModel.category == category).all()
        return result

    def create_movie(self, data: Movie):
        # Convertimos del esquema validador al modelo de la base de datos
        new_movie = MovieModel(**data.model_dump())
        self.db.add(new_movie)
        self.db.commit()
        return True
    
    def update_movie(self, id: int, data: Movie):
        movie = self.get_movie(id)
        if not movie:
            return False
        
        movie.title = data.title
        movie.overview = data.overview
        movie.year = data.year
        movie.rating = data.rating
        movie.category = data.category
        
        self.db.commit()
        return True
    
    def delete_movie(self, id: int):
        movie = self.get_movie(id)
        if not movie:
            return False
        self.db.delete(movie)
        self.db.commit()
        return True
        
