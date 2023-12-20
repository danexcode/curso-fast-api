from fastapi import FastAPI, status
from fastapi.responses import HTMLResponse

from config.database import engine, Base
from middlewares.error_handler import ErrorHandler
from routers.movie import movie_router
from routers.user import user_router

app = FastAPI()
app.add_middleware(ErrorHandler)
app.include_router(movie_router)
app.include_router(user_router)
app.title = "Mi aplicacion con FastAPI"
app.version = "0.0.1"

Base.metadata.create_all(bind=engine)


@app.get(path="/", summary="Index", tags=["Index"], status_code=status.HTTP_200_OK)
def message():
    return HTMLResponse("<h1>Hola Mundo!!</h1>")
