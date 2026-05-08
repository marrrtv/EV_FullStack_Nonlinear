from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from app.db.dependencies import get_db
from app.services.product_service import get_productos
from app.schemas.productos import ProductoResponse

router = APIRouter(prefix="/productos", tags=["productos"]) #tags para la doc. automatica

@router.get("/", response_model=list[ProductoResponse])
def list_products(
    categoria: str | None = None,
    skip: int = Query(0, ge=0, description="Registros a saltar"),
    limit: int = Query(100, ge=1, le=1000, description="Máximo de registros"),
    db: Session = Depends(get_db)
):
    """Lista todos los productos con filtrado y paginación opcional"""
    try:
        return get_productos(db, categoria= categoria, skip=skip, limit=limit)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))