# 📊 Pratique o conhecimento em criação de graficos a parti de um datafreme

Este projeto implementa um dashboard interativo em Python utilizando Dash e Plotly

## 📋 Sobre o Projeto

O dashboard apresenta 7 gráficos interativos:
- Histograma – Distribuição de descontos aplicados
- Gráfico de Dispersão – Relação entre preço e número de avaliações
- Mapa de Calor – Correlação entre variáveis numéricas
- Gráfico de Barras – Top 10 marcas mais frequentes
- Gráfico de Pizza – Distribuição de produtos por gênero
- Gráfico de Densidade – Distribuição de preços
- Regressão Linear – Relação entre preço e desconto
## 🛠 Tecnologias Utilizadas

- **Python 3**
- **Dash criação da - aplicação web interativa
- **Plotly Express - visualizações interativas
- **Pandas - manipulação e análise de dados
- **Statsmodel - suporte à regressão linear

## 📁 Estrutura do Projeto
PROJETO_EBAC_GRAFICOS_DASH/
│
├── README.md                  # Documentação principal
│
├── 📂 projeto_grafico_dash
│   └── ecommerce_estatistica.csv   # Dataset principal
│   └── projeto 3.py              # Script de análise principal
└


## ▶️ Como Executar o Projeto
1. Clone o repositório
git clone https://github.com/seu-usuario/dashboard-ecommerce.git
cd dashboard-ecommerce

2. Crie um ambiente virtual (opcional, mas recomendado)
python -m venv .venv
source .venv/bin/activate   # Linux/Mac
.venv\Scripts\activate      # Windows

3. Instale as dependências
pip install -r requirements.txt


Caso não tenha o requirements.txt, instale manualmente:

pip install dash plotly pandas statsmodels

4. Execute o servidor local
python app.py

5. Acesse no navegador
http://127.0.0.1:8050/
