from jwt import encode, decode

def create_token(data: dict):
    token = encode(payload=data, key="mySecret", algorithm="HS256")
    return token

def validate_token(token: str) -> dict:
    payload: dict = decode(token, "mySecret", algorithms=["HS256"])
    return payload