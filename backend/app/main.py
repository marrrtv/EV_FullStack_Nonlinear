import logging
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.db.base import Base
from app.db.session import engine, SessionLocal
from app.db.seed import seed_database

# IMPORTANTE: Importar TODOS los modelos antes de crear las tablas
import app.models.categorias
import app.models.productos
import app.models.movimientos  

from app.routes.productos import router as productos_router

# configurar logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# crear tablas con los modelos ORM sqlalchemy
Base.metadata.create_all(bind=engine) # en un proyecto real utilizaría migraciones con Alembic para versionar cambios de esquema.
logger.info("Tablas de BD creadas/verificadas")

# lifespan para manejar startup y shutdown de la aplicación
@asynccontextmanager
async def lifespan(app: FastAPI):

    # startup: Inicializar datos
    db = SessionLocal()
    try:
        seed_database(db)
        logger.info("Seed de base de datos completado")
    except Exception as e:
        logger.error(f"Error en seed: {str(e)}")
    finally:
        db.close()
    
    yield
    
    # shutdown
    logger.info("API cerrándose")

app = FastAPI(
    title="API Gestión de Inventario",
    description="API para gestionar productos, categorías y movimientos de inventario",
    version="1.0.0",
    lifespan=lifespan
)

# CORS configuration
origins = ["http://localhost:5173"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(productos_router)

@app.get("/")
def root():
    """Health check de la API"""
    return {"message": "API running", "version": "1.0.0"}

