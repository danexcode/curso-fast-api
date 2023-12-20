from pydantic import BaseModel, Field
from typing import Optional

class Movie(BaseModel):
    id: Optional[int] = None
    title: str = Field(min_length=3, max_length=15)
    overview: str = Field(
        default="Descripcion de la película", min_length=15, max_length=50
    )
    year: int = Field(default=2023, le=2023)
    rating: float = Field(ge=1, le=10)
    category: str = Field(min_length=3, max_length=10)

    model_config = {
        "json_schema_extra": {
            "examples": [
                {
                    "title": "Mi Pelicula",
                    "overview": "Descripcion de la pelicula",
                    "year": 2022,
                    "rating": 9.9,
                    "category": "Acción",
                }
            ]
        }
    }