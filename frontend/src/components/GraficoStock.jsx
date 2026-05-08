import {BarChart, Bar, XAxis, YAxis, Tooltip, ResponsiveContainer, Cell, LabelList} from "recharts";

// recibe la lista de productos y genera un gráfico de barras con el stock total por categoría, 
// indicando con una alerta si alguna categoría tiene productos con stock bajo

// => solo recibe datos y los muestra
function GraficoStock({ productos }) {

  // agrupar productos por categoría
  const categoriasMap = {};

  productos.forEach((producto) => {

    const categoria = producto.categoria;

    // si la categoría no existe todavía, la creamos
    if (!categoriasMap[categoria]) {

      categoriasMap[categoria] = {
        categoria: categoria,
        stockTotal: 0,
        tieneStockBajo: false,
      };
    }

    // acumulamos stock
    categoriasMap[categoria].stockTotal += producto.stock_actual;

    // verificamos si algún producto tiene stock bajo
    if (
      producto.stock_actual < producto.stock_minimo
    ) {
      categoriasMap[categoria].tieneStockBajo = true;
    }
  });

  // convertir objeto a array porque recharts espera un array
  const datos_grafico = Object.values(categoriasMap);

  // colores por categoría
  const colores = [
    "#2563eb",
    "#16a34a",
    "#9333ea",
    "#ea580c",
    "#db2777",
    "#0891b2",
  ];

  return (

    // devolvemos el grafico que va a ir al costado del listado de productos, 
    // con un título y una explicación de la alerta
    <aside className="bg-white rounded-xl shadow-sm p-6 h-[400px] min-w-0">

      <h2 className="text-2xl font-semibold mb-2">
        Stock por categoría
      </h2>

      <p className="text-gray-500 mb-6">
        Stock total agrupado por categoría
      </p>

      <ResponsiveContainer width="100%" height={280}>

        <BarChart data={datos_grafico}>

          <XAxis dataKey="categoria" />

          <YAxis />

          <Tooltip />

          <Bar dataKey="stockTotal">

            <LabelList
              dataKey="tieneStockBajo"
              position="top"
              formatter={(value) =>
                value ? "⚠" : ""
              }
            />

            {datos_grafico.map((entry, index) => (

              <Cell // cada barra tendrá un color diferente según su categoría
                key={entry.categoria}
                fill={
                  colores[index % colores.length] // reutiliza colores si hay muchas categorías
                }
              />

            ))}

          </Bar>

        </BarChart>

      </ResponsiveContainer>

      <div className="mt-4 text-sm text-gray-600 flex items-center gap-2">

        <span className="text-yellow-500 text-lg">
          ⚠
        </span>

        <p className="text-base">
          Las categorías con alerta tienen
          al menos un producto con stock bajo.
        </p>

      </div>

    </aside>
  );
}

export default GraficoStock;