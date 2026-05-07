from sqlalchemy import CheckConstraint, Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

from app.db import Base

class Producto(Base):
    __tablename__ = "producto"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(200), nullable=False, index=True)
   
    precio_unitario = Column(Float, nullable=False)  # no debe ser null, y debe ser >= 0
    stock_actual = Column(Integer, default=0, nullable=False)  # debe ser >= 0
    stock_minimo = Column(Integer, default=0, nullable=False)  # debe ser >= 0

    id_categoria = Column(Integer,
                          ForeignKey("categoria.id"),
                          nullable=False) #no debe ser null

    # Relationships
    category = relationship("categoria")
    movimientos = relationship("movimiento", back_populates="product")

    # Definir la restricción check
    __table_args__ = (
        CheckConstraint('stock_minimo >= 0', name='stock_minimo_mayor_o_igual_a_0'),
        CheckConstraint('stock_actual >= 0', name='stock_actual_mayor_o_igual_a_0'),
        CheckConstraint('precio_unitario >= 0', name='precio_unitario_mayor_o_igual_a_0'),
    )
