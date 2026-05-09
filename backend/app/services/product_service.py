from app.schemas.productos import ProductResponse

# bd mockeada 
mock_products = [
    {
        "id": 1,
        "nombre": "Notebook Lenovo",
        "precio_unitario": 1200,
        "stock_actual": 7,
        "stock_minimo": 5,
        "categoria": {
            "id": 1,
            "nombre": "Electronica"
        }
    },
    {
        "id": 2,
        "nombre": "Mouse Logitech",
        "precio_unitario": 50,
        "stock_actual": 9,
        "stock_minimo": 10,
        "categoria": {
            "id": 1,
            "nombre": "Electronica"
        }
    },
    {
        "id": 3,
        "nombre": "Silla Oficina",
        "precio_unitario": 300,
        "stock_actual": 5,  
        "stock_minimo": 2,
        "categoria": {
            "id": 2,
            "nombre": "Muebles"
        }
    },
    {
        "id": 4,
        "nombre": "Escritorio Oficina",
        "precio_unitario": 1000,
        "stock_actual": 18,  
        "stock_minimo": 5,
        "categoria": {
            "id": 2,
            "nombre": "Muebles"
        }
    },
    {
        "id": 5,
        "nombre": "Papel A4",
        "precio_unitario": 136,
        "stock_actual": 5,  
        "stock_minimo": 1,
        "categoria": {
            "id": 3,
            "nombre": "Papeleria"
        }
    },
    {
        "id": 6,
        "nombre": "Lapiceras Azules",
        "precio_unitario": 15,
        "stock_actual": 5,  
        "stock_minimo": 20,
        "categoria": {
            "id": 3,
            "nombre": "Papeleria"
        }
    },
    {
        "id": 7,
        "nombre": "Lapiceras Rojas",
        "precio_unitario": 17,
        "stock_actual": 35,  
        "stock_minimo": 20,
        "categoria": {
            "id": 3,
            "nombre": "Papeleria"
        }
    }
]


def get_productos(category: str | None = None):

    if category:
        filtered_products = [
            product
            for product in mock_products
            if product["categoria"]["nombre"].lower() == category.lower()
        ]
    else:
        filtered_products = mock_products

    response = []
    for product in filtered_products:
        response.append(
            ProductResponse(
                id=product["id"],
                nombre=product["nombre"],
                precio_unitario=product["precio_unitario"],
                stock_actual=product["stock_actual"],
                stock_minimo=product["stock_minimo"],
                categoria=product["categoria"]["nombre"]
            )
        )

    return response
