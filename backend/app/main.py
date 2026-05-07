from fastapi import FastAPI

from app.db.base import Base
from app.db.session import engine
import app.models.categorias
import app.models.productos

from app.routes.productos import router as productos_router

app = FastAPI()

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(productos_router)

@app.get("/")
def root():
    return {"message": "API running"}