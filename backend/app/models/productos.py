from sqlalchemy import CheckConstraint, String, ForeignKey, String, ForeignKey, Numeric, CheckConstraint
from decimal import Decimal
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base
# from app.models.productos import Categoria
# from app.models.movimientos import Movimiento

class Producto(Base):
    __tablename__ = "productos"

    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(150), nullable=False)
    
    # --> producto pertenece a una sola categoría y no puede quedar sin una asignada (nullable=False)
    categoria_id: Mapped[int] = mapped_column(ForeignKey("categorias.id"), nullable=False)
    
    # --> precio unitario no nulo. Numeric(10, 2) es mejor que float y la mejor práctica para dinero
    precio_unitario: Mapped[Decimal] = mapped_column(Numeric(10, 2), nullable=False)
    stock_actual: Mapped[int] = mapped_column(default=0, nullable=False)
    stock_minimo: Mapped[int] = mapped_column(default=0, nullable=False)

    # relaciones: acá le estamos diciendo a Python qué tipo de objeto nos va a devolver cuando accedamos a esa propiedad.
    # 1-N:
    categoria: Mapped["Categoria"] = relationship(back_populates="productos")
    # N-1:
    movimientos: Mapped[list["Movimiento"]] = relationship(back_populates="producto")

    # reglas de negocio a nivel BD
    __table_args__ = (
        # el stock de un producto nunca puede quedar en negativo
        CheckConstraint("stock_actual >= 0", name="check_stock_no_negativo"),
        CheckConstraint("stock_minimo >= 0", name="check_stockminimo_no_negativo"),
        # regla implicita: el precio no debe ser negativo
        CheckConstraint("precio_unitario > 0", name="check_precio_positivo"),
    )
