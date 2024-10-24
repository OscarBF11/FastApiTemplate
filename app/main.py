from fastapi import FastAPI
from contextlib import asynccontextmanager
from app.database import engine

# Asegurar la conexión a la base de datos y mostrar un mensaje de éxito
def verify_database_connection():
    try:
        with engine.connect() as connection:
            print("Successfully connected to the database.")
    except Exception as e:
        print(f"Error connecting to the database: {e}")

# Definir el ciclo de vida de la aplicación
@asynccontextmanager
async def lifespan(app: FastAPI):
    verify_database_connection()
    yield
    print("Closing API.")

# Crear la aplicación FastAPI con ciclo de vida definido
app = FastAPI(lifespan=lifespan)

# Primer endpoint
@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI!"}
