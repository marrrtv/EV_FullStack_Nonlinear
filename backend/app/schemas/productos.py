from pydantic import BaseModel

class ProductResponse(BaseModel):

    id: int
    nombre: str
    precio_unitario: float
    stock_actual: int
    stock_minimo: int
    categoria: str

    class Config:
        from_attributes = True