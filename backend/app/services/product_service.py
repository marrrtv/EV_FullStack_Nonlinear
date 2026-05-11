import logging
from sqlalchemy import select
from sqlalchemy.orm import Session, selectinload
from app.models.productos import Producto
from app.models.categorias import Categoria  

logger = logging.getLogger(__name__)

# Implementé acá la interacción con la base de datos para obtener los productos,
# y no en una capa mas baja, porque no es necesario tener una capa de repositorio
# para esta versión simple de la aplicación, evito agregar complejidad innecesaria.

def get_productos(db: Session, categoria: str | None = None,
) -> list[Producto]:
   
    try: # utilizar try-except para capturar errores de BD

        stmt = select(Producto).options(selectinload(Producto.categoria)) # cargar la categoría relacionada en la misma consulta para evitar N+1
        
        if categoria: # si se especifica un filtro de categoría, hacer un join con la tabla de categorías y filtrar por nombre
            stmt = stmt.join(Producto.categoria).where(
                Categoria.nombre.ilike(f"%{categoria}%")
            )
        
        productos = db.scalars(stmt).all() # ejecutar la consulta y obtener los resultados como una lista de objetos Producto
        logger.info(f"Se obtuvieron {len(productos)} productos de la BD (categoría: {categoria or 'todas'})")
        return productos
        
    except Exception as e:
        logger.error(f"Error al obtener productos: {str(e)}")
        raise