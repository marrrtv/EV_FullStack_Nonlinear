from pydantic import BaseModel

class ProductResponse(BaseModel):

    id: int
    name: str
    current_stock: int
    category: str

    class Config:
        from_attributes = True