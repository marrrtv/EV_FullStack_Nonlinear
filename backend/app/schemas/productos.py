from pydantic import BaseModel

class ProductoRespuesta(BaseModel):
    id: int
    nombre: str
    categoria: str  # Category name
    precio_unit: float
    stock_actual: int
    stock_minimo: int

