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
#---

## 🛠️ Tecnologias Utilizadas

- [Python 3.10+](https://www.python.org/)  
- [Dash](https://dash.plotly.com/) → criação da aplicação web interativa  
- [Plotly Express](https://plotly.com/python/plotly-express/) → visualizações interativas  
- [Pandas](https://pandas.pydata.org/) → manipulação e análise de dados  
- [Statsmodels](https://www.statsmodels.org/stable/index.html) → suporte à regressão linear  
- [NumPy](https://numpy.org/) → cálculos numéricos  

---

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

### 1. Clone o repositório
```bash
git clone https://github.com/gustavoboag/PROJETO_EBAC_GRAFICOS_DASH.git
cd dashboard-ecommerce 
```
2. Crie um ambiente virtual (opcional, mas recomendado)
```bash
python -m venv .venv
source .venv/bin/activate   # Linux/Mac
.venv\Scripts\activate      # Windows
```

3. Instale as dependências
```bash
pip install dash plotly pandas statsmodels
```

4. Execute o servidor local
```bash
python projeto 3.py

```
5. Acesse no navegador
cpp
http://127.0.0.1:9050/
```
