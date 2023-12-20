from fastapi import APIRouter, Query, Path, Depends
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from typing import List

from config.database import Session
from schemas.movie import Movie
from models.movie import Movie as MovieModel
from middlewares.jwt_bearer import JWTBearer
from services.movie import MovieService

movie_router = APIRouter()
service = MovieService()


@movie_router.get(
    "/movies", tags=["movies"], response_model=List[Movie], status_code=200
)
def get_movies() -> List[Movie]:
    result = service.get_movies()
    return JSONResponse(content=jsonable_encoder(result), status_code=200)


@movie_router.get("/movies/{id}", tags=["movies"], response_model=Movie)
def get_movie(id: int = Path(ge=1, le=2000)) -> Movie:
    result = service.get_movie(id)
    if not result:
        return JSONResponse(status_code=404, content={"message": "not found"})
    return JSONResponse(status_code=200, content=jsonable_encoder(result))


@movie_router.get("/movies/", tags=["movies"], response_model=List[Movie])
def get_movies_by_category(
    category: str = Query(min_length=5, max_length=15)
) -> List[Movie]:
    result = service.get_movies_by_category(category)
    return JSONResponse(status_code=200, content=jsonable_encoder(result))


@movie_router.post(
    "/movies",
    tags=["movies"],
    response_model=dict,
    status_code=201,
    # dependencies=[Depends(JWTBearer())],
)
def create_movie(movie: Movie) -> dict:
    service.create_movie(movie)
    return JSONResponse(
        content={"message": "Se ha creado la pelicula"}, status_code=201
    )


@movie_router.put(
    "/movies/{id}", tags=["movies"], response_model=List[Movie], status_code=200
)
def update_movie(id: int, data: Movie) -> List[Movie]:
    result = service.update_movie(id, data)
    if not result:
        return JSONResponse(status_code=404, content={"message": "not found"})
    return JSONResponse(status_code=200, content={"message": "updated!"})


@movie_router.delete("/movies/{id}", tags=["movies"], response_model=List[Movie])
def delete_movie(id: int) -> List[Movie]:
    result = service.delete_movie(id)
    if not result:
        return JSONResponse(status_code=404, content={"message": "not found"})
    return JSONResponse(status_code=200, content={"message": "deleted!"})
