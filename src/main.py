from fastapi import FastAPI, Response, Cookie, Depends, status, HTTPException
from fastapi.security import HTTPBasic, HTTPBasicCredentials

from schemas import User

app = FastAPI()
security = HTTPBasic

USER_DATA = [User(**{"username": "user1", "password": "pass1"}), User(**{"username": "user2", "password": "pass2"})]


def get_user_from_db(username: str):
    print(username, "FUCK")
    for user in USER_DATA:
        if user.username == username:
            return user
    return None

def authenticate_user(credentials: HTTPBasicCredentials = Depends(security)):
    if credentials.username:
        user = get_user_from_db(credentials.username)
        if user is None or user.password != credentials.password:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid credentials", headers={"WWW-Authenticate": "Basic"})
        return user
    return None

@app.get("/login")
async def login(user: User = Depends(authenticate_user)):
    return {"message": "You got my secret, welcome"}

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