from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.dependencies import get_db
from app.services.product_service import get_productos
from app.schemas.productos import ProductoResponse

router = APIRouter(prefix="/productos", tags=["productos"]) #tags para la doc. automatica

@router.get("/", response_model=list[ProductoResponse])
def list_products(
    categoria: str | None = None,
    db: Session = Depends(get_db)
):
    try:
        return get_productos(db, categoria= categoria) 
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))