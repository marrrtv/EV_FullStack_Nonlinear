from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.dependencies import get_db
from app.services.product_service import get_productos
from app.schemas.productos import ProductResponse

router = APIRouter(prefix="/productos", tags=["productos"]) #tags para la doc. automatica

@router.get("/", response_model=list[ProductResponse]) #response_model para la doc. automatica, y para validar la respuesta
def list_products(categoria: str | None = None, db: Session = Depends(get_db)): # usa depends para inyectar la sesión de base de datos
    return get_productos(categoria)
    # return get_productos(db, categoria) #--> funcion de servicio, que se encarga de la lógica de negocio, y a su vez llama al repositorio para obtener los datos.