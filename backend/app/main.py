from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.db.base import Base
from app.db.session import engine

from app.routes.productos import router as productos_router

app = FastAPI()

# CORS configuration para definir origens permitidas, métodos y headers

origins = [ "http://localhost:5173" ]  # origen del frontend, esto cambia en producción

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(productos_router)

#version 1
@app.get("/v1/")
def root():
    return {"message": "API running"}