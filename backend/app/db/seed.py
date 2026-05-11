# backend/app/db/seed.py
import logging
from sqlalchemy.orm import Session
from app.models.categorias import Categoria
from app.models.productos import Producto
from decimal import Decimal

logger = logging.getLogger(__name__)

def seed_database(db: Session):
    """
    Inicializa la BD con categorías y productos por defecto.
    Solo crea si no existen.
    """
    
    # Verificar si ya hay categorías
    if db.query(Categoria).count() > 0:
        logger.info("Base de datos ya tiene categorías, skipeando seed")
        return
    
    try:
        # Crear categorías
        categorias = [
            Categoria(nombre="Electronica", descripcion="Dispositivos electrónicos"),
            Categoria(nombre="Muebles", descripcion="Muebles de oficina"),
            Categoria(nombre="Papeleria", descripcion="Artículos de papelería"),
        ]
        
        for cat in categorias:
            db.add(cat)
        db.commit()
        logger.info("Categorías creadas")
        
        # Crear productos
        productos = [
            Producto(
                nombre="Notebook Lenovo",
                categoria_id=1,
                precio_unitario=Decimal("1200.00"),
                stock_actual=7,
                stock_minimo=5
            ),
            Producto(
                nombre="Mouse Logitech",
                categoria_id=1,
                precio_unitario=Decimal("50.00"),
                stock_actual=9,
                stock_minimo=10
            ),
            Producto(
                nombre="Silla Oficina",
                categoria_id=2,
                precio_unitario=Decimal("300.00"),
                stock_actual=5,
                stock_minimo=2
            ),
            Producto(
                nombre="Escritorio Oficina",
                categoria_id=2,
                precio_unitario=Decimal("1000.00"),
                stock_actual=18,
                stock_minimo=5
            ),
            Producto(
                nombre="Papel A4",
                categoria_id=3,
                precio_unitario=Decimal("136.00"),
                stock_actual=5,
                stock_minimo=1
            ),
            Producto(
                nombre="Lapiceras Azules",
                categoria_id=3,
                precio_unitario=Decimal("15.00"),
                stock_actual=5,
                stock_minimo=20
            ),
            Producto(
                nombre="Lapiceras Rojas",
                categoria_id=3,
                precio_unitario=Decimal("17.00"),
                stock_actual=35,
                stock_minimo=20
            ),
        ]
        
        for prod in productos:
            db.add(prod)
        db.commit()
        logger.info(f"Se crearon {len(productos)} productos de prueba")
        
    except Exception as e:
        db.rollback()
        logger.error(f"Error al hacer seed de la BD: {str(e)}")
        raise