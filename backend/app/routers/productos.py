from fastapi import APIRouter

router = APIRouter(prefix="/productos", tags=["productos"]) #tags para la doc. automatica

@router.get("/")
def list_productos():
   return {"message": "Lista de productos"}
