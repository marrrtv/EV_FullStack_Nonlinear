import { useState, useEffect } from "react";
import {BarChart, Bar, XAxis, YAxis, Tooltip, ResponsiveContainer, Cell} from "recharts";

// componente que representa cada item de producto, recibe props con la info del producto
function ProductosItems({
  id,
  nombre,
  precio,
  descripcion,
  categoria,
  stock,
  stock_minimo,
}) {

  // creo variable booleana para determinar si indicar que el stock es bajo o no
  const stockBajo = stock < stock_minimo;
  // => React renderiza cosas distintas según condiciones

  return ( 
    // className son clases de Tailwind, cada clase agrega un estilo.

    // <article className="bg-white text-gray-800 rounded-xl shadow-md p-5 flex flex-col gap-3 hover:shadow-lg transition">
    <article className="bg-white text-gray-800 rounded-xl shadow-sm p-4 flex items-center justify-between hover:shadow-md transition">
      {/* article ya que representa un elemento de contenido independiente y reutilizable (item producto) */}
      <div className="flex items-center gap-10 flex-1">

        <div className="w-48">
          <h2 className="font-semibold text-lg">
            {id} - {nombre}
          </h2>

          <p className="text-sm text-gray-500">
            {categoria}
          </p>
        </div>

        <p className="text-gray-700 flex-1">
          {descripcion}
        </p>

        <p className="font-semibold w-24">
          ${precio}
        </p>

        <p className="w-24">
          Stock: <span className="font-semibold">{stock}</span>
        </p>

        <span
          className={`px-3 py-1 rounded-full text-sm font-medium ${
            stockBajo
              ? "bg-red-100 text-red-700"
              : "bg-green-100 text-green-700"
          }`}
        >
          {stockBajo ? "Stock bajo" : "Disponible"}
        </span>

      </div>

      <button className="ml-6 bg-gray-500 text-white px-4 py-2 rounded-lg hover:bg-gray-700 transition">
        Ver más
      </button>

    </article>
  );
}

// funcion que se corre al iniciar la app, se encarga de mostrar el listado de productos obtenidos del backend
function App() {

  // [valor/estado, funcionParaActualizarlo] = useState(valorInicial)
  const [productos, setProductos] = useState([]); // empieza vacio al iniciar la app 

  // funcion para obtener los productos del backend, es async porque hace una petición a un servidor, y esa petición tarda un tiempo en responder => usa async/await para manejar esa asincronía
  const fetchProductos = async () => {

    // como vamos a hacer una petición a un servidor y puede haber errores => manejo de errores con try/catch
    try {
      // fetch hace una request HTTP al backend a la ruta /productos, que devuelve un JSON con el listado de productos
      const response = await fetch(
        "http://localhost:8000/productos"
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
                id={producto.id}
                nombre={producto.nombre}
                precio={producto.precio_unitario}
                descripcion={producto.descripcion}
                categoria={producto.categoria.nombre}
                stock={producto.stock_actual}
                stock_minimo={producto.stock_minimo}
              />

            ))}

          </section>
          
          <aside className="bg-white rounded-xl shadow-sm p-5 w-1/3 h-[500px]">

            <h2 className="text-xl font-semibold mb-6">
              Stock por producto
            </h2>

            <ResponsiveContainer width="100%" height="90%"> 
              {/* hace que el gráfico se adapte automáticamente al tamaño */}

              <BarChart data={productos}>
                {/* crea grafico de barras usando el estado de react */}

                <XAxis dataKey="nombre" />

                <YAxis />

                <Tooltip />

                <Bar dataKey="stock_actual">

                  {productos.map((producto) => (

                    <Cell
                      key={producto.id}
                      fill={
                        producto.stock_actual < producto.stock_minimo
                          ? "#c41818"
                          : "#08a52d"
                      }
                    />

                  ))}

                </Bar>

              </BarChart>

            </ResponsiveContainer>

          </aside>
        </div>
      )}
    </main>
  );
}

export default App;