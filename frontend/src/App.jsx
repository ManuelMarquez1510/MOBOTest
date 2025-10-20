import React from "react";
import AppLayout from "./layouts/AppLayout";
import ControlPanelView from "./views/ControlPanelView";
import "./App.css";

function App() {
  return (
    <AppLayout>
      <ControlPanelView />
    </AppLayout>
  );
}

export default App;
