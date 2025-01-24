from fastapi import FastAPI, Response, Cookie, Depends, status, HTTPException
from fastapi.security import HTTPBasic, HTTPBasicCredentials, OAuth2PasswordBearer
from datetime import datetime, timezone, timedelta

import jwt

from schemas import User

app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")
# security = HTTPBasic

SECRET_KEY = "baa944b6ea3b7c9f904d0d8b873503d5fc70379e415ae9ca0296f56ec5bac5a8"
ALGORITHM = "HS256"

USERS_DATA = [User(**{"username": "user1", "password": "pass1"}), 
             User(**{"username": "user2", "password": "pass2"})]


def get_user_from_db(username: str):
    for user in USERS_DATA:
        if user.username == username:
            return user
    return None

def create_jwt_token(data: dict):
    return jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)

def get_user_from_token(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM]) # декодируем токен
        return payload.get("sub") # тут мы идем в полезную нагрузку JWT-токена и возвращаем утверждение о юзере (subject); обычно там еще можно взять "iss" - issuer/эмитент, или "exp" - expiration time - время 'сгорания' и другое, что мы сами туда кладем
    except jwt.ExpiredSignatureError:
        return {"error": "token expired"}
        pass # тут какая-то логика ошибки истечения срока действия токена
    except jwt.InvalidTokenError:
        return {"error": "invalid token"}
        pass # тут какая-то логика обработки ошибки декодирования токена


@app.post("/login")
async def login(user_in: User): 
    for user in USERS_DATA:
        if user.username == user_in.username and user.password == user_in.password:
            return {"access_token": create_jwt_token({"sub": user_in.username, "exp": datetime.now(tz=timezone.utc) + timedelta(seconds=50)}), "token_type": "bearer"}
    return {"error": "Invalid credentials"}

@app.get("/about_me")
async def about_me(current_user: str = Depends(get_user_from_token)):
    user = get_user_from_db(current_user)
    if user:
        return {"message": "good"}
    return current_user

# def authenticate_user(credentials: HTTPBasicCredentials = Depends(security)):
#     try:
#         username = credentials.username
#     except AttributeError:
#         print("there is no username")
#         return None
#     if username:
#         user = get_user_from_db(username)
#         if user is None or user.password != credentials.password:
#             raise HTTPException(
#                 status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid credentials", headers={"WWW-Authenticate": "Basic"})
#         return user
#     return None

# @app.get("/login")
# async def login(user: User | None = Depends(authenticate_user)):
#     return {"message": "You got my secret, welcome"}

@app.get("/logout")
def logout():
    raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="You have successfully logged out",
            headers={"WWW-Authenticate": "Basic"},
        )


# @app.post("/login")
# async def login(user: User, response: Response):
#     if user.username == "andrew" and user.password == "123":
#         response.set_cookie(key="session_token", value="abc123xyz456")
#         return {"message": "Куки установлены"}
#     return {"message": "Неверные данные"}

@app.get("/")
async def root(session_token = Cookie(default=None)):
    return {"session_token": session_token}

@app.post("/calculate")
async def calculate(num1: int, num2: int):
    return {"answer": num1+num2}