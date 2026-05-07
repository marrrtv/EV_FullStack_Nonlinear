from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship, Mapped, mapped_column

from app.db.base import Base
from app.models.productos import Producto

class Categoria(Base):
    __tablename__ = "categorias"

    id: Mapped[int] = mapped_column(primary_key=True)
    nombre: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)
    descripcion: Mapped[str | None] = mapped_column(String(255)) # Mapped[str | None] lo entiende tanto SQLAlchemy como Python y luego Pydantic, y permite que el campo sea opcional (nullable) en la base de datos. 

    # N-1:
    productos: Mapped[list["Producto"]] = relationship(back_populates="categoria")
    # no crea columnas reales en la base de datos, pero sirve para hacer consultas complejas con FastAPI 
