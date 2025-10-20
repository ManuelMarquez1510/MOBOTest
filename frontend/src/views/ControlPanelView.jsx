import React, { useEffect, useState } from "react";
import "./ControlPanelView.css";
import BeachList from "../components/ItemList";
import MOCK from "../utils/json";

const ControlPanelView = () => {
  const [counter, setCounter] = useState({
    total: 0,
    activos: 0,
    inactivos: 0,
  });

  // Se raliza el conteo del total de items de cada estado
  useEffect(() => {
    const total = MOCK.length;
    const activos = MOCK.filter((item) => item.status.toLowerCase() === "activo").length;
    const inactivos = MOCK.filter((item) => item.status.toLowerCase() === "inactivo").length;

    setCounter({ total, activos, inactivos });
  }, []);

  return (
    <div className="control-panel">
      <h1>Cosas de playa</h1>

      <div className="panel-cards">
        <div className="panel-card">
          <h3>Activos</h3>
          <p className="card-number">{counter.activos}</p>
        </div>
        <div className="panel-card">
          <h3>Inactivos</h3>
          <p className="card-number">{counter.inactivos}</p>
        </div>
        <div className="panel-card">
          <h3>Total</h3>
          <p className="card-number">{counter.total}</p>
        </div>
      </div>

      <BeachList />
    </div>
  );
};

export default ControlPanelView;
