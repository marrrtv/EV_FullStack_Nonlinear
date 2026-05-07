from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.dependencies import get_db
from app.services.product_service import get_products

router = APIRouter(prefix="/productos", tags=["productos"]) #tags para la doc. automatica

@router.get("/")
def list_products(category: str | None = None, db: Session = Depends(get_db)): # usa depends para inyectar la sesión de base de datos
    return get_products(category)
    # return get_products(db, category) #--> funcion de servicio, que se encarga de la lógica de negocio, y a su vez llama al repositorio para obtener los datos.