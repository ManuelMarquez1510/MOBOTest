import React from "react";
import "./Navbar.css";

const Navbar = ({ toggleSidebar, isMobile }) => {
  return (
    <header className="navbar-header">
      <div className="navbar-content">
        <div className="navbar-left">
          {isMobile && (
            <button className="navbar-toggle" onClick={toggleSidebar}>
              <span className="hamburger"></span>
              <span className="hamburger"></span>
              <span className="hamburger"></span>
            </button>
          )}
          <h1>Panel de Control</h1>
        </div>
      </div>
    </header>
  );
};

export default Navbar;
