import React, { useEffect, useState } from "react";
import JSON from "../utils/json";
import "./ItemList.css";
// listado de los status
const STATUS_OPTIONS = [
  { label: "Todos", value: "todos" },
  { label: "Activo", value: "activo" },
  { label: "Inactivo", value: "inactivo" },
];

const ItemList = () => {
  const [items, setItems] = useState([]);
  const [loading, setLoading] = useState(true);
  const [filter, setFilter] = useState("todos");

  // Se realiza la simulacion de una peticion GET de los items
  useEffect(() => {
    const timer = setTimeout(() => {
      setItems(JSON);
      setLoading(false);
    }, 350);
    timer;
  }, []);

  // Se inicializan todos los elementos al inicio, despues se mostrara de acuerdo eleccion del usuario
  const filteredItems = items.filter((item) => {
    return filter === "todos" || item.status === filter;
  });

  return (
    <div className="item-list">
      <div className="item-controls">
        <div className="control-group">
          <label>Filtrar por estado</label>
          <select value={filter} onChange={(e) => setFilter(e.target.value)}>
            {STATUS_OPTIONS.map((option) => (
              <option key={option.value} value={option.value}>
                {option.label}
              </option>
            ))}
          </select>
        </div>
      </div>

      {loading ? (
        <div className="item-empty">Cargando...</div>
      ) : (
        <ul className="item-grid">
          {filteredItems.map((item) => (
            <li key={item.id} className={`item-card ${item.status}`}>
              <div className="item-card-header">
                <h4 className="item-title">{item.name}</h4>
                <span className={`status ${item.status}`}>{item.status === "activo" ? "Activo" : "Inactivo"}</span>
              </div>
              <p className="item-desc">{item.description ? item.description : "Sin descripcion"}</p>
              <div className="item-meta">
                <span className="meta-date">{new Date(item.created_at).toLocaleDateString()}</span>
              </div>
            </li>
          ))}
        </ul>
      )}
    </div>
  );
};

export default ItemList;
