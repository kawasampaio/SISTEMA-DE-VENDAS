import pandas as pd
import matplotlib.pyplot as plt

def calculate_revenue(data):
    """
    Calcula a renda total por variação.
    :param data: DataFrame com as colunas ['Produto', 'Variação', 'Quantidade', 'Preço Unitário']
    :return: DataFrame com as colunas ['Variação', 'Renda Total']
    """
    data['Renda'] = data['Quantidade'] * data['Preço Unitário']
    revenue = data.groupby('Variação')['Renda'].sum().reset_index()
    revenue = revenue.sort_values(by='Renda', ascending=False)
    return revenue

def plot_revenue(revenue_data):
    """
    Gera um gráfico de barras mostrando a renda por variação.
    :param revenue_data: DataFrame com as colunas ['Variação', 'Renda Total']
    """
    plt.figure(figsize=(10, 6))
    plt.bar(revenue_data['Variação'], revenue_data['Renda'], color='skyblue')
    plt.title('Renda por Variação')
    plt.xlabel('Variação')
    plt.ylabel('Renda Total')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()
