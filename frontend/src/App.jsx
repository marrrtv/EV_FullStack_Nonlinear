import { useState, useEffect } from "react";
import {BarChart, Bar, XAxis, YAxis, Tooltip, ResponsiveContainer, Cell} from "recharts";
import optionsIcon from "./assets/options_icon.png";

// imports de los componentes de la UI
import MovimientoForm from "./components/MovimientoForm";
import ProductosItems from "./components/ProductosItems";
import GraficoStock from "./components/GraficoStock";

// funcion que se corre al iniciar la app, se encarga de mostrar el listado de productos obtenidos del backend
function App() {

  // [valor/estado, funcionParaActualizarlo] = useState(valorInicial)
  const [productos, setProductos] = useState([]); // empieza vacio al iniciar la app 
  const [productoSeleccionado, setProductoSeleccionado] = useState(null); // para manejar el producto seleccionado y mostrar el formulario de movimiento


  // funcion para obtener los productos del backend, es async porque hace una petición a un servidor, y esa petición tarda un tiempo en responder => usa async/await para manejar esa asincronía
  const fetchProductos = async () => {

    // como vamos a hacer una petición a un servidor y puede haber errores => manejo de errores con try/catch
    try {
      // fetch hace una request HTTP al backend a la ruta /productos, que devuelve un JSON con el listado de productos
      const response = await fetch(
        "http://localhost:8000/v1/productos"
      );

      const productosJSON = await response.json();

      // imprimo el JSON que me devuelve el backend para verificar que estoy recibiendo los datos correctamente
      console.log(productosJSON);

      // Esto es EL corazón de React --> actualizamos el estado definido antes => react actualiza la UI
      setProductos(productosJSON);
    
    } catch (error) {

      // si hay un error en la petición, lo capturamos y lo mostramos por consola
      console.error(
        "Error fetching productos:",
        error
      );
    }
  };

  // Ejecutar solo una vez cuando el componente se monta --> llamamos a fetchProductos para obtener los datos del backend justo después de que la app se inicia
  useEffect(() => {
    fetchProductos();
  }, []);

  return ( // devuelve la UI que se va a renderizar, un listado de productos con estilos de Tailwind
    <main className="min-h-screen bg-gray-100 p-8">

      <header className="mb-10">

        <h1 className="text-4xl font-bold text-gray-900">
          Sistema de Inventario
        </h1>

        <p className="text-gray-600 mt-2">
          Gestión de productos y stock
        </p>

      </header>

      {productos.length === 0 ? (

        <p className="text-gray-600">
          Cargando productos...
        </p>

      ) : (

        <div className="flex gap-8 items-start">
          {/*<section className="flex flex-col gap-4"> */}
          <section className="flex flex-col gap-4 w-2/3">

            {productos.map((producto) => (
              // iteramos sobre el array de productos obtenido del backend, 
              // y por cada producto renderizamos un componente ProductosItems definido arriba, 
              // pasando la info del producto como props
              
              <ProductosItems
                key={producto.id}
                producto={producto} // pasamos para poder actualizar el producto seleccionado al hacer click en el boton def dentro de ProductosItems
                setProductoSeleccionado={setProductoSeleccionado}
                nombre={producto.nombre}
                precio={producto.precio_unitario}
                categoria={producto.categoria.nombre}
                stock={producto.stock_actual}
                stock_minimo={producto.stock_minimo}
              />

            ))}

          </section>
          
          <GraficoStock productos={productos} />
          

          {/* renderizado condicional --> mostrar el formulario SOLO si hay producto seleccionado */}
          {productoSeleccionado && (

            <MovimientoForm // es un modal (ventana emergente) para registrar un movimiento de stock
              producto={productoSeleccionado}
              setProductoSeleccionado={setProductoSeleccionado}
            />

          )}

        </div>
      )}
    </main>
  );
}

export default App;