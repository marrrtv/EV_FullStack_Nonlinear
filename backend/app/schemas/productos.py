from pydantic import BaseModel
from decimal import Decimal

from .categorias import CategoriaResponse  

class ProductoResponse(BaseModel):
    id: int
    nombre: str
    precio_unitario: float
    stock_actual: int
    stock_minimo: int
    categoria: CategoriaResponse  # Ahora es un objeto

    class Config:
        from_attributes = True
