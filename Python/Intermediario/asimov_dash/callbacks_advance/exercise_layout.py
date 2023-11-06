from dash import Dash, html, dcc
import plotly.express as px
import dash_bootstrap_components as dbc
import pandas as pd

# ---- Configuration ---- #
app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
server = app.server

# -> Dataframe:
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

lista_de_cidades = {
    'Brasil': ['Rio de Janeiro', 'Minas Gerais', 'Paraná'],
    'Canada': [u'Montréal', 'Toronto', 'Ottawa']
}
# -> Figure:
fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")
fig.update_layout(
    plot_bgcolor='#111111',
    paper_bgcolor='#111111',
    font_color='#7FDBFF'
)

# -> Cartão:
card_content = [
    dbc.CardHeader('Cartão'), # => Cabeçalho
    dbc.CardBody([
        html.H5('Titulo do Cartão', className='card-title'),
        html.P('conteudo', className='card-title')
    ])
]



app.layout = html.Div(children=[
        dbc.Row([
            # -> Menu:
            dbc.Col([
                dbc.Card([
                    dbc.CardBody([
                        html.H2('CodeLinx', style={'font-family':'voltaire', 'font-size': '60px'}),
                        html.P('Isso é um template'),
                    dcc.RadioItems(
                        id='countries-radio',
                        options=[{f'label': k, 'value': k} for k in lista_de_cidades.keys()],
                        value='Brasil'),                    
                    ])
                ],color='primary', style={'margin': '15px 0px 0px 15px', 'height': '90vh', 'padding-left': '10px'}),
            ], md=2, style={'margin': 'px'}),
            # -> Fig1
            dbc.Col([
                dbc.Row([
                    dbc.Col([dcc.Graph(id='1', figure=fig, style={'height': '20vh'})], md=4),
                    dbc.Col([dcc.Graph(id='2', figure=fig, style={'height': '20vh'})], md=4),
                    dbc.Col([dcc.Graph(id='3', figure=fig, style={'height': '20vh'})], md=4),]),
                dbc.Row([
                    dbc.Col([dcc.Graph(id='4', figure=fig, style={'height': '35vh'})], md=12),]),
                dbc.Row([
                    dbc.Col([dcc.Graph(id='5', figure=fig, style={'height': '40vh'})], md=12),]),
            ],md=10)
        ])
    ])

# ---- Start Server ---- #
if __name__ == '__main__':
    app.run_server(debug=True)