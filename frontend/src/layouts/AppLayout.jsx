import React, { useState, useEffect } from "react";
import Navbar from "../components/Navbar";
import Sidebar from "../components/Sidebar";
import "./AppLayout.css";

function AppLayout({ children }) {
  const [isSidebarOpen, setIsSidebarOpen] = useState(false);
  const [isMobile, setIsMobile] = useState(false);

  // Se identifica si es el tamaño de la pantalla es movil, ademas de que cada vez que se cambie el tamaño de la pantalla se identifique nuevamente
  useEffect(() => {
    const isMobile = () => {
      setIsMobile(window.innerWidth <= 768);
      // Cuando no es celular, siempre mantener el sidebar abierto
      if (window.innerWidth > 768) {
        setIsSidebarOpen(true);
      } else {
        setIsSidebarOpen(false);
      }
    };

    isMobile();
    window.addEventListener("resize", isMobile);
  }, []);

  const toggleSidebar = () => {
    setIsSidebarOpen(!isSidebarOpen);
  };

  const closeSidebar = () => {
    if (isMobile) {
      setIsSidebarOpen(false);
    }
  };

  return (
    <div className="layout-container">
      <Navbar toggleSidebar={toggleSidebar} isMobile={isMobile} />

      <div className="layout-main">
        <Sidebar isOpen={isSidebarOpen} onClose={closeSidebar} />

        <section className="layout-content">{children}</section>
      </div>
    </div>
  );
}

export default AppLayout;
