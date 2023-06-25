# ---- Import Libs ---- #
from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

# ---- Configurations ---- #
# -> Instance:
app = Dash(__name__)
# -> Dataframe:
df = pd.DataFrame({
    'Frutas': ['Maças', 'Laranjas', 'Bananas','Maças', 'Laranjas', 'Bananas'],
    'Quantidade': [4,1,2,2,4,5],
    'Cidade': ['DF','DF','DF','SP','SP','SP']    
})
# -> Figure:
fig = px.bar(df, x='Frutas', y='Quantidade', color='Cidade')

# ---- Layout ---- #
app.layout = html.Div(id='title',
    children=[
        html.H1('Dash Python'),
        html.Div('Dash: Framework web para Python', style={'color': '#FFF444'}),
        dcc.Graph(figure=fig, id='graph_bar')
    ]
)

# ---- Start Server ---- #
if __name__ == '__main__':
    app.run_server(debug=True)