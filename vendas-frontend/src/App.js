import React from 'react';
import RegisterSale from './components/RegisterSale'; // Importando o componente

function App() {
  return (
    <div className="App">
      <h1>Cadastro de Vendas</h1>
      <RegisterSale />  {/* Usando o componente */}
    </div>
  );
}

export default App;
