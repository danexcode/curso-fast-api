from fastapi import APIRouter
from fastapi.responses import JSONResponse

from utils.jwt_manager import create_token
from schemas.user import User

user_router = APIRouter()

@user_router.post("/login", tags=["auth"])
def login(user: User):
    if user.email == "admin@gmail.com" and user.password == "admin":
        # .model_dump lo que hace es convetir user a diccionario
        token = create_token(user.model_dump())
        return JSONResponse(status_code=200, content=token)
    return JSONResponse(status_code=401, content={"message": "Unauthorized"})