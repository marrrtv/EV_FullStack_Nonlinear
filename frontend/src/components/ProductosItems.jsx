import optionsIcon from "../assets/options_icon.png";
import { useState, useEffect } from "react";
import {BarChart, Bar, XAxis, YAxis, Tooltip, ResponsiveContainer, Cell} from "recharts";

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

    // <article className="bg-white text-gray-800 rounded-xl shadow-md p-5 flex flex-col gap-3 hover:shadow-lg transition">
    <article className="bg-white text-gray-800 rounded-xl shadow-sm py-2 px-4 flex items-center justify-between hover:shadow-md transition">
      {/* article ya que representa un elemento de contenido independiente y reutilizable (item producto) */}
      <div className="flex items-center gap-10 flex-1">

        <div className="w-48">
          <h2 className="font-semibold text-lg">
            {nombre}
          </h2>
        </div>
       
        <p className="text-sm text-gray-500">
              {categoria}
            </p>

        {/* <p className="text-gray-700 flex-1">
          {descripcion}
        </p> */}

        <p className="font-semibold w-24">
          ${precio} <span className="font-light text-sm">(c/u)</span>
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

      <button
        onClick={() =>
          setProductoSeleccionado(producto)
        }
        className="ml-6 bg-gray-500 text-white px-4 py-2 rounded-lg hover:bg-gray-700 transition">
        
        <img
          src={optionsIcon}
          className="w-5 h-5"
        />
      </button>

    </article>
  );
}

export default ProductosItems;