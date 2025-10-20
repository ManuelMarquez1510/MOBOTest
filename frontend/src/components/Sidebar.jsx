import React, { useState, useEffect } from "react";
import "./Sidebar.css";

const Sidebar = ({ isOpen, onClose }) => {
  const [isMobile, setIsMobile] = useState(false);
  // Se identifica si es el tamaño de la pantalla es movil, ademas de que cada vez que se cambie el tamaño de la pantalla se identifique nuevamente
  useEffect(() => {
    const isMobile = () => {
      setIsMobile(window.innerWidth <= 768);
    };

    isMobile();
    window.addEventListener("resize", isMobile);
  }, []);

  const items = [{ name: "Home", id: "home" }];

  return (
    <>
      {isOpen && <div className="sidebar-overlay" onClick={onClose}></div>}

      <aside className={`sidebar ${isOpen ? "sidebar-open" : ""}`}>
        {isMobile && (
          <div className="sidebar-header">
            <button className="sidebar-close" onClick={onClose}>
              <span>×</span>
            </button>
          </div>
        )}

        <nav className="sidebar-nav">
          <ul>
            {items.map((item) => (
              <li key={item.id} className={"active"}>
                {item.name}
              </li>
            ))}
          </ul>
        </nav>
      </aside>
    </>
  );
};

export default Sidebar;
