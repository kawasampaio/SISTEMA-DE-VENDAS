import React, { useState } from 'react';
import axios from 'axios';

const RegisterSale = () => {
  const [produto, setProduto] = useState('');
  const [quantidade, setQuantidade] = useState('');
  const [variacao, setVariacao] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const response = await axios.post("http://127.0.0.1:5000/register_sale", {
        produto,
        quantidade,
        variacao
      });
      console.log('Venda registrada:', response.data);
    } catch (error) {
      console.error('Erro ao registrar venda:', error);
    }
  };

  return (
    <div>
      <h2>Registrar Venda</h2>
      <form onSubmit={handleSubmit}>
        <div>
          <label>Produto:</label>
          <input
            type="text"
            value={produto}
            onChange={(e) => setProduto(e.target.value)}
            required
          />
        </div>
        <div>
          <label>Quantidade:</label>
          <input
            type="number"
            value={quantidade}
            onChange={(e) => setQuantidade(e.target.value)}
            required
          />
        </div>
        <div>
          <label>Variação:</label>
          <input
            type="text"
            value={variacao}
            onChange={(e) => setVariacao(e.target.value)}
            required
          />
        </div>
        <button type="submit">Registrar</button>
      </form>
    </div>
  );
};

export default RegisterSale;
