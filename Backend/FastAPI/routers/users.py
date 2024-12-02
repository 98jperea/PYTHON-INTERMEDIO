from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import APIRouter


app = FastAPI()

router = APIRouter()

class User(BaseModel):
    id: int
    Nombre: str
    Apellido: str
    Edad: int
    Ciudad: str

users_list = [User(id=1, Nombre="Jose", Apellido="Perea", Edad=26, Ciudad="Sevilla"),
         User(id=2, Nombre="Carlos", Apellido="García", Edad=40, Ciudad="Caracas")]


@router.get("/usersjson")
async def usersjson():
    return [
        {"Nombre":"Jose", "Apellido":"Perea", "Edad":26, "Ciudad":"Sevilla"},
        {"Nombre":"Carlos", "Apellido":"García", "Edad":40, "Ciudad":"Caracas"}
    ]

@router.get("/user")
async def users():
    return users_list

@router.get("/user/{id}")
async def user(id:int):
    users = filter(lambda user:user.id == id, users_list)
    
    try:
        return list(users)[0]
    except:
        return {"Error":"No se ha encontrado el usuario"}

#Prueba (por mi parte)
"""
@app.get("/user2/{id}")
async def user(id:int):
    users = filter(lambda user:user.id == id, users_list)
    return list(users)
"""
"""
@app.get("/userquery/{id}")
async def user(id:int):
    users = filter(lambda user:user.id == id, users_list)
    
    try:
        return list(users)[0]
    except:
        return {"Error":"No se ha encontrado el usuario"}
"""
"""
@app.get("/user/{id}")
async def user(id:int):

def search_user(id:int)
    users = filter(lambda user:user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"Error":"No se ha encontrado el usuario"}
"""

@router.get("/user/{id}")
async def user (id: int):
    return search_user(id)

@router.get("/user")
async def user(id: int):
    return search_user(id)

def search_user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error": "No se ha encontrado el usuario"}
    
#Operaciones POST, PUT y DELETE

@router.post("/user/")
async def user(user: User):
    if type(search_user(user.id)) == User:
        return {"error": "El usuario ya existe"} 
    else:
        users_list.append(user)
        return user
@router.put("/user/")
async def user(user: User):

    found = False

    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            users_list[index] = user
            found = True

@router.delete("/user/{id}")
async def user(id: int):
    for index, saved_user in enumerate(users_list):
        if saved_user.id == user.id:
            del users_list[index]
            found = True

        if not found:
            return {"error":"No se ha eliminado el usuario"}

def search_user(id: int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"error": "No se ha encontrado el usuario"}
    
