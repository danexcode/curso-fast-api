from fastapi import Request, HTTPException
from fastapi.security import HTTPBearer

from utils.jwt_manager import validate_token

class JWTBearer(HTTPBearer):
    # defino una funcion para obtener la peticion del usuario
    async def __call__(self, request: Request):
        # llamo al metodo call en la clase HTTPBearer para obtener las credenciales (token)
        auth = await super().__call__(request)
        data = validate_token(auth.credentials)
        if data["email"] != "admin@gmail.com":
            raise HTTPException(status_code=403, detail="Credenciales invalidas")