import logging
from sqlalchemy import select
from sqlalchemy.orm import Session, selectinload
from app.models.productos import Producto
from app.models.categorias import Categoria  

logger = logging.getLogger(__name__)


# def get_productos(
#     db: Session, 
#     categoria: str | None = None, 
#     skip: int = 0, 
#     limit: int = 100
# ) -> list[Producto]:
#     """
#     Obtiene productos de la BD real con filtrado opcional por nombre de categoría y paginación.
    
#     Args:
#         db: Sesión de BD
#         categoria: Nombre de la categoría para filtrar (opcional)
#         skip: Saltar N registros (para paginación)
#         limit: Cantidad máxima de registros a retornar
#     """
#     try:
#         stmt = select(Producto)
        
#         if categoria:
#             stmt = stmt.join(Producto.categoria).where(
#                 Categoria.nombre.ilike(f"%{categoria}%")
#             )
        
#         stmt = stmt.offset(skip).limit(limit)
#         productos = db.scalars(stmt).all()
#         logger.info(f"Se obtuvieron {len(productos)} productos de la BD (categoría: {categoria or 'todas'})")
#         return productos
        
#     except Exception as e:
#         logger.error(f"Error al obtener productos: {str(e)}")
#         raise


def get_productos(
    db: Session, 
    categoria: str | None = None, 
    skip: int = 0, 
    limit: int = 100
) -> list[Producto]:
    """
    Obtiene productos de la BD real con filtrado opcional por nombre de categoría y paginación.
    
    Args:
        db: Sesión de BD
        categoria: Nombre de la categoría para filtrar (opcional)
        skip: Saltar N registros (para paginación)
        limit: Cantidad máxima de registros a retornar
    """
    try:
        stmt = select(Producto).options(selectinload(Producto.categoria))
        
        if categoria:
            stmt = stmt.join(Producto.categoria).where(
                Categoria.nombre.ilike(f"%{categoria}%")
            )
        
        stmt = stmt.offset(skip).limit(limit)
        productos = db.scalars(stmt).all()
        logger.info(f"Se obtuvieron {len(productos)} productos de la BD (categoría: {categoria or 'todas'})")
        return productos
        
    except Exception as e:
        logger.error(f"Error al obtener productos: {str(e)}")
        raise