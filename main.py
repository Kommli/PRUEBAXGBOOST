from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

#http://127.0.0.1:8000

class Libro(BaseModel):
    titulo: str
    desc: str
    price: int
    marco_tela: bool

@app.get("/")
def index():
    return {"Mensaje":"Hola mundo"}

@app.get("/modelo/{id}&{precio}")

def mostrarLibros(id: int, precio: int):
    return {"Libro":id, "Precio": precio}

@app.post("/libros")
def insertar_libros(Libro: Libro):
    return {"message": f"libro {Libro.titulo} insertadoooo"}