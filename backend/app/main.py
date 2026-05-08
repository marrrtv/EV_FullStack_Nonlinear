import logging
from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.db.base import Base
from app.db.session import engine
from app.db.seed import seed_database
from app.db.session import SessionLocal


# IMPORTANTE: Importar TODOS los modelos antes de crear las tablas
import app.models.categorias
import app.models.productos
import app.models.movimientos  # ← FALTABA ESTE

from app.routes.productos import router as productos_router

# Configurar logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# Reemplazar la línea de crear tablas con:
Base.metadata.create_all(bind=engine)
logger.info("Tablas de BD creadas/verificadas")
# Lifespan event para inicializar datos
@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: Inicializar datos
    db = SessionLocal()
    try:
        seed_database(db)
        logger.info("Seed de base de datos completado")
    except Exception as e:
        logger.error(f"Error en seed: {str(e)}")
    finally:
        db.close()
    
    yield
    
    # Shutdown
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

