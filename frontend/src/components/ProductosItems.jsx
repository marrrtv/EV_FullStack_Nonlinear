import optionsIcon from "../assets/options_icon.png";
import { useState, useEffect } from "react";

// componente que representa cada item de producto, recibe props con la info del producto
function ProductosItems({
  id,
  producto,
  setProductoSeleccionado,
  nombre,
  precio,
  categoria,
  stock,
  stock_minimo,
}) {

  // creo variable booleana para determinar si indicar que el stock es bajo o no
  const stockBajo = stock < stock_minimo;
  // => React renderiza cosas distintas según condiciones

  return ( 
    // className son clases de Tailwind, cada clase agrega un estilo.
    <article className="bg-white text-gray-800 rounded-xl shadow-sm py-2 px-4 hover:shadow-md transition">

      <div className="grid grid-cols-[2fr_1fr_1fr_1fr_1fr_auto] items-center gap-4">

        <div>
          <h2 className="font-semibold text-lg">
            {nombre}
          </h2>
        </div>

        <p className="text-sm text-gray-500">
          {categoria.toUpperCase()}
        </p>

        <p className="font-semibold">
          ${precio} <span className="font-light text-sm">(c/u)</span>
        </p>

        <p>
          Stock: <span className="font-semibold">{stock}</span>
        </p>

        <div>
          <span
            className={`px-3 py-1 rounded-full text-sm font-medium whitespace-nowrap ${
              stockBajo
                ? "bg-red-100 text-red-700"
                : "bg-green-100 text-green-700"
            }`}
          >
            {stockBajo ? "Stock bajo" : "Disponible"}
          </span>
        </div>

        <button
          onClick={() =>
            setProductoSeleccionado(producto)
          }
          className="bg-gray-500 text-white px-4 py-2 rounded-lg hover:bg-gray-700 transition"
        >
          <img
            src={optionsIcon}
            className="w-5 h-5"
          />
        </button>

      </div>

    </article>
  );
}

export default ProductosItems;