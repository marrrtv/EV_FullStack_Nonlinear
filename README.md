# Sistema de Gestión de Inventario - Ejercicio de Evaluación Técnica

**Full Stack Junior Evaluation | Nonlinear | 2026**

---

# Descripción del Proyecto

Sistema web completo para la gestión de inventario de productos que permite:

- Listar productos con información de categoría, precio y stock
- Visualizar alertas de stock bajo
- Registrar movimientos de inventario (entradas y salidas) --> solo frontend
- Filtrar productos por categoría --> solo backend
- Visualizar gráficos de stock en tiempo real

---

# Stack Tecnológico

## Backend

- **Framework:** FastAPI
- **Base de Datos:** PostgreSQL
- **ORM:** SQLAlchemy 2.0+ 
- **Validación:** Pydantic v2
- **Servidor:** Uvicorn

## Frontend

- **Framework UI:** React 19.2
- **Build Tool:** Vite
- **Estilos:** Tailwind CSS
- **Gráficos:** Recharts
- **Servidor Dev:** Vite Dev Server

---

# Estructura del Proyecto

```txt
EV_FullStack_Nonlinear/
├── backend/
│   ├── app/
│   │   ├── main.py                    # Punto de entrada FastAPI
│   │   ├── db/
│   │   │   ├── base.py               # Configuración base SQLAlchemy
│   │   │   ├── session.py            # Engine y SessionLocal
│   │   │   ├── dependencies.py       # Inyección de dependencias
│   │   │   └── seed.py               # Datos iniciales
│   │   ├── models/                   # Modelos SQLAlchemy (ORM)
│   │   │   ├── productos.py
│   │   │   ├── categorias.py
│   │   │   └── movimientos.py
│   │   ├── routes/                   # Endpoints FastAPI
│   │   │   └── productos.py
│   │   ├── schemas/                  # Modelos Pydantic (validación)
│   │   │   ├── productos.py
│   │   │   └── categorias.py
│   │   └── services/                 # Lógica de negocio
│   │       └── product_service.py
│   └── requirements.txt
├── frontend/
│   ├── src/
│   │   ├── main.jsx                  # Entry point
│   │   ├── App.jsx                   # Componente principal
│   │   ├── index.css                 # Estilos globales
│   │   ├── components/               # Componentes React
│   │   │   ├── ProductosItems.jsx
│   │   │   ├── MovimientoForm.jsx
│   │   │   └── GraficoStock.jsx
│   │   └── assets/
│   ├── index.html
│   ├── package.json
│   ├── vite.config.js
│   ├── tailwind.config.js
│   └── postcss.config.js
└── docker-compose.yml                 # Place holder para una futura dockerización
```

---

# Decisiones Técnicas Principales

## 1. FastAPI 

- Validación automática con Pydantic
- Documentación OpenAPI automática
- Buena performance
- Ideal para APIs REST modernas

---

## 2. SQLAlchemy 2.0 con Type Hints

```python
stmt = select(Producto).options(selectinload(Producto.categoria))
productos = db.scalars(stmt).all()
```

- Type safety completo
- Mejor soporte del IDE y autocompletado
- Código más limpio y mantenible

---

## 3. Modelo de Datos Robusto

### Restricciones a nivel base de datos

```python
__table_args__ = (
    CheckConstraint("stock_actual >= 0", name="check_stock_no_negativo"),
    CheckConstraint("precio_unitario > 0", name="check_precio_positivo"),
)
```

- Integridad de datos garantizada en la base de datos
- No depender únicamente de validaciones de backend
- Prevención de estados inválidos

### Tipos de datos apropiados

- `Numeric(10, 2)` para precios (**NO float**)
- `Enum` para tipos de movimiento
- `DateTime(timezone=True)` para timestamps

---

## 4. CORS habilitado para desarrollo

Uso de `CORSMiddleware` en FastAPI para permitir requests desde:

```txt
http://localhost:5173
```

---

# Instalación y Ejecución

## Requisitos Previos

- Python 3.10+
- Node.js 18+
- PostgreSQL 12+
- Git

---

# 1. Configurar Backend

```bash
cd backend

# Crear entorno virtual
python -m venv venv

# Activar entorno virtual
# Windows:
venv\Scripts\activate

# Linux / Mac:
source venv/bin/activate

# Instalar dependencias
pip install -r requirements.txt
```

## Crear archivo `.env`

```env
DATABASE_URL=postgresql://user:password@localhost:5432/inventario_db
```

## (Opcional) Crear base de datos

```bash
psql -U postgres -c "CREATE DATABASE inventario_db;"
```

---

# Iniciar Backend

```bash
uvicorn app.main:app --reload
```

Backend disponible en:

```txt
http://localhost:8000
```

Documentación Swagger:

```txt
http://localhost:8000/docs
```

---

# 2. Configurar Frontend

```bash
cd frontend

# Instalar dependencias
npm install

# Iniciar servidor de desarrollo
npm run dev
```

Frontend disponible en:

```txt
http://localhost:5173
```

---

# Docker

La estructura del proyecto permite una futura dockerización del sistema completo sencilla. Se deja el docker-compose.yml como placeholder.

---

# Endpoints de la API implementado

## Productos

### `GET /productos`

Lista productos con filtrado y paginación.

### Query Parameters

| Parámetro | Tipo | Descripción |
|---|---|---|
| categoria | string | Filtrar por categoría |
| skip | int | Registros a saltar |
| limit | int | Máximo de registros |

### Ejemplo de respuesta

```json
[
  {
    "id": 1,
    "nombre": "Laptop",
    "precio_unitario": 999.99,
    "stock_actual": 5,
    "stock_minimo": 2,
    "categoria": {
      "id": 1,
      "nombre": "Electrónica"
    }
  }
]
```

---

# Componentes Frontend

## `ProductosItems.jsx`

Tarjeta individual de producto que muestra:

- Nombre y categoría
- Precio unitario
- Stock actual
- Badge de estado ("Disponible" / "Stock bajo")
- Botón de opciones --> por ahora solo lleva al frontend de "Registrar Movimiento"

---

## `MovimientoForm.jsx`

Formulario modal para registrar:

- Entradas de stock
- Salidas de stock
- Validaciones de stock negativo

---

## `GraficoStock.jsx`

Gráfico realizado con Recharts para visualizar:

- Stock agrupado por categoría
- Alertas visuales de stock bajo

---

# Características Implementadas

## Backend 

- Modelos SQLAlchemy con Type Hints
- Constraints y validaciones a nivel BD
- Endpoints FastAPI
- Validación Pydantic
- CORS configurado
- Logging básico
- Seed de datos iniciales
- Servicios separados de las rutas
- Manejo de errores

---

## Frontend 

- Listado de productos
- Indicadores visuales de stock bajo
- Componentes reutilizables
- Fetch API para comunicación con backend
- Modal para registrar movimientos
- Validaciones de formulario

---