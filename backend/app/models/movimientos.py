from datetime import datetime
import enum

from sqlalchemy import String, ForeignKey, DateTime, Enum, CheckConstraint
from sqlalchemy.sql import func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base
from app.models.productos import Producto

class TipoMovimiento(enum.Enum):
    ENTRADA = "entrada"
    SALIDA = "salida"

class Movimiento(Base):
    __tablename__ = "movimientos"

    id: Mapped[int] = mapped_column(primary_key=True)
    producto_id: Mapped[int] = mapped_column(ForeignKey("productos.id"), nullable=False)
    
    # acá usamos la clase definida arriba para restringir los tipos de movimiento a nivel de código y base de datos
    tipo: Mapped[TipoMovimiento] = mapped_column(Enum(TipoMovimiento), nullable=False)
    cantidad: Mapped[int] = mapped_column(nullable=False)
    
    # server_default=func.now() asegura que la BD le asigne la fecha exacta de inserción.
    fecha: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    
    motivo: Mapped[str | None] = mapped_column(String(255))
    
    # por ahora usuario es un string simple, pero querríamos relacionarlo con una tabla de usuarios
    usuario_id: Mapped[str] = mapped_column(String(100), nullable=False)

    # Relación
    producto: Mapped["Producto"] = relationship(back_populates="movimientos")

    __table_args__ = (
        # previene que se registren movimientos con cantidad 0 o negativa por error
        CheckConstraint("cantidad > 0", name="check_cantidad_positiva"),
    )