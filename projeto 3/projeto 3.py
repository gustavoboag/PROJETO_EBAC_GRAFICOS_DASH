import pandas as pd
from dash import Dash, dcc, html
import plotly.express as px

# Carrega dataset
df = pd.read_csv('ecommerce_estatistica.csv')

# Preparação do dataframe para gráfico de pizza
df['Gênero_Agrupado'] = df['Gênero'].replace({
    'Meninos': 'Masculino',
    'Meninas': 'Feminino',
    'Sem gênero infantil': 'Sem gênero',
    'Bebês': 'Sem gênero',
    'Unissex': 'Sem gênero',
    'roupa para gordinha pluss P ao 52': 'Sem gênero',
    'Sem gênero': 'Sem gênero'
})

# Cria app Dash
app = Dash(__name__)

app.layout = html.Div([
    html.H1("Projeto de graficos usando o dash 'EBAC'", style={'textAlign': 'center'}),

    # Gráficos
    dcc.Graph(id='grafico-histogram-desconto'),
    dcc.Graph(id='grafico-scatter-preco-avaliacoes'),
    dcc.Graph(id='grafico-heatmap-corr'),
    dcc.Graph(id='grafico-bar-top-marcas'),
    dcc.Graph(id='grafico-pizza-genero'),
    dcc.Graph(id='grafico-densidade-preco'),
    dcc.Graph(id='grafico-regressao-preco-desconto')
])


# Função para gerar todos os gráficos
def gerar_graficos(df_filtrado):
    # 1. Histograma de Descontos
    fig_hist = px.histogram(
        df_filtrado,
        x='Desconto',
        nbins=15,
        title='Distribuição de Descontos Aplicados',
        marginal='box',
        color_discrete_sequence=['#DC143C']
    )

    # 2. Scatter Preço vs Número de Avaliações
    fig_scatter = px.scatter(
        df_filtrado,
        x='Preço',
        y='N_Avaliações',
        color='Gênero_Agrupado',
        title='Preço vs Número de Avaliações'
    )

    # 3. Heatmap de correlação
    numeric_cols = ['Nota', 'N_Avaliações', 'Desconto', 'Preço', 'Qtd_Vendidos_Cod']
    corr = df_filtrado[numeric_cols].corr()
    fig_heatmap = px.imshow(corr, text_auto='.2f', color_continuous_scale='RdBu_r', origin='lower',
                            title='Mapa de Calor - Correlação entre Variáveis')

    # 4. Top 10 marcas por frequência
    top_marcas = df_filtrado['Marca'].value_counts().head(10).reset_index()
    top_marcas.columns = ['Marca', 'Quantidade']
    fig_bar = px.bar(top_marcas, x='Marca', y='Quantidade', title='Top 10 Marcas Mais Frequentes', color='Marca')

    # 5. Gráfico de Pizza por Gênero
    genero_dist = df_filtrado['Gênero_Agrupado'].value_counts().reset_index()
    genero_dist.columns = ['Gênero', 'Quantidade']
    fig_pie = px.pie(
        genero_dist,
        names='Gênero',
        values='Quantidade',
        title='Distribuição de Produtos por Gênero',
        color_discrete_sequence=['#66b3ff', '#ff9999', '#99ff99']
    )

    # 6. Densidade de Preço
    fig_density = px.histogram(
        df_filtrado,
        x='Preço',
        nbins=30,
        histnorm='density',
        title='Densidade de Distribuição de Preços',
        marginal='box',
        color_discrete_sequence=['purple']
    )

    # 7. Regressão Preço vs Desconto
    fig_reg = px.scatter(
        df_filtrado,
        x='Preço',
        y='Desconto',
        color='Gênero_Agrupado',
        trendline='ols',
        title='Relação: Preço vs Desconto Aplicado'
    )

    return fig_hist, fig_scatter, fig_heatmap, fig_bar, fig_pie, fig_density, fig_reg


# Preenche os gráficos ao carregar a página
figs = gerar_graficos(df)
app.layout.children[1].figure = figs[0]
app.layout.children[2].figure = figs[1]
app.layout.children[3].figure = figs[2]
app.layout.children[4].figure = figs[3]
app.layout.children[5].figure = figs[4]
app.layout.children[6].figure = figs[5]
app.layout.children[7].figure = figs[6]

# Executa app
if __name__ == '__main__':
    app.run(debug=True, port=9050)
