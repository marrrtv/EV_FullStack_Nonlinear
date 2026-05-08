import { useState } from "react";


// crea la ventana modal para registrar un movimiento de stock, 
// recibe como props el producto seleccionado y la función para actualizarlo 
// (para cerrar el modal al cancelar o guardar)
function MovimientoForm({
  producto,
  setProductoSeleccionado,
}) {

    const [tipoMovimiento, setTipoMovimiento] = useState("Entrada");

    const [cantidad, setCantidad] = useState(1);

    const [errorStock, setErrorStock] = useState("");

    const manejarGuardado = (e) => {

        e.preventDefault(); // evitar que el formulario recargue la página

        // validación stock negativo
        if (
            tipoMovimiento === "Salida" &&
            cantidad > producto.stock_actual
        ) {

            setErrorStock(
            "No hay stock suficiente para realizar esta salida (Stock actual: " +
                producto.stock_actual + ")"
            );

            return; // detiene la ejecución si hay error, no guarda el movimiento ni cierra el modal
        }

        // limpiar error si todo ok
        setErrorStock("");

        ///////////////////////////////////////////////////////////////////////////////
        // acá iría la lógica para guardar el movimiento (llamar a una API del backend)
        ///////////////////////////////////////////////////////////////////////////////

        console.log("Movimiento guardado");

        // cerrar modal
        setProductoSeleccionado(null);
        };

  return (

    // fixed = el elemento “flota” sobre toda la pantalla
    // inset-0 = ocupa toda la pantalla (top:0, left:0, right:0, bottom:0)
    // bg-black = fondo oscuro transparente
    // z-50 = hace que el modal quede por ENCIMA de todo
    <div className="fixed inset-0 bg-black/40 flex items-center justify-center z-50">

      {/* ventana modal */}
      <div className="bg-white rounded-2xl shadow-xl w-full max-w-lg p-8">

        <div className="flex justify-between items-center mb-6">

          <h2 className="text-2xl font-bold text-gray-800">
            Registrar movimiento
          </h2>

        </div>

        <div className="mb-6">

          <p className="text-gray-600 text-sm">
            Producto seleccionado
          </p>

          <p className="font-semibold text-lg">
            {producto.nombre}
          </p>

        </div>


        <form
            onSubmit={manejarGuardado}  // al hacer submit (click en guardar) se ejecuta la función manejarGuardado definida arriba
            className="flex flex-col gap-4">

          {/* tipo movimiento */}
          <div>

            <label className="block text-sm font-medium mb-1">
              Tipo de movimiento
            </label>

            <select // select muestra un recuadro de selección con opciones
              className="w-full border rounded-lg px-3 py-2"
              value={tipoMovimiento}
              onChange={(e) => setTipoMovimiento(e.target.value)} // cada vez que cambia react actualiza estado.
            >

              <option>
                Entrada
              </option>

              <option>
                Salida
              </option>

            </select>

          </div>

          {/* cantidad */}
          <div>

            <label className="block text-sm font-medium mb-1">
              Cantidad
            </label>

            <input
              type="number"
              min="1"
              className="w-full border rounded-lg px-3 py-2"
              value={cantidad}
              onChange={(e) => setCantidad(Number(e.target.value))} //lo pasamos a numero      
            />

            {/* mostrar error si hay */}
            {errorStock && (

            <div className="bg-red-100 border border-red-300 text-red-700 px-4 py-2 rounded-lg text-sm">

                {errorStock}

            </div>

            )}
          </div>
          

          {/* motivo */}
          <div>

            <label className="block text-sm font-medium mb-1">
              Motivo
            </label>

            <textarea
              rows="3"
              className="w-full border rounded-lg px-3 py-2"
            />

          </div>

          {/* botones */}
          <div className="flex justify-end gap-3 mt-4">

            <button
              type="button"
              onClick={() =>
                setProductoSeleccionado(null)
              }
              className="px-4 py-2 rounded-lg border hover:bg-gray-100"
            >
              Cancelar
            </button>

            <button
              type="submit"
              className="px-4 py-2 rounded-lg bg-gray-800 text-white hover:bg-gray-700"
            >
              Guardar movimiento
            </button>

          </div>

        </form>

      </div>

    </div>
  );
}

export default MovimientoForm;