# Panel de Control Frontend (React + Vite)

Aplicacion React con Vite que implementa un panel de control y area de contenido. Incluye un listado con filtro por estado, diseño responsive

## Requisitos

- Node.js >= 18.x (recomendado LTS)
- npm >= 9.x

## Instalación

```bash
npm install
```

## Desarrollo

```bash
npm run dev
```

- La app corre por defecto en `http://localhost:5173`.

## Estructura relevante

```
src/
  components/
    Navbar.jsx
    Navbar.css
    Sidebar.jsx
    Sidebar.css
    ItemList.jsx          # Listado con filtro
    ItemList.css
  layouts/
    Applayout.jsx
    AppLayout.css
  views/
    ControlPanelView.jsx  # Vista principal 
    ControlPanelView.css
  utils/
    json.js               # Fuente de datos simulada 
  App.jsx
  main.jsx
```


