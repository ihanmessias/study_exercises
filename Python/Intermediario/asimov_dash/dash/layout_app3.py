# ---- Import Libs ---- #
import dash
from dash import html, dcc

# https://dash.plotly.com/dash-core-components
# https://dash.plotly.com/dash-html-components
# ---- Configuration ---- #
# -> External Style:
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
# ---- Layout ---- #
app.layout = html.Div([
    html.Label('Dropdown'),
    dcc.Dropdown(
        options=[
            {'label': 'Rio Grande do Sul', 'value': 'NYC'},
            {'label': 'São Paulo', 'value': 'SP'},
            {'label': 'Santa Catarina', 'value': 'SC'}
        ],
        value='SP', style={'margin-bottom': '50px'}
    ),

    html.Label('Multi-Select Dropdown'),
    dcc.Dropdown(
        options=[
            {'label': 'Rio Grande do Sul', 'value': 'NYC'},
            {'label': 'São Paulo', 'value': 'SP'},
            {'label': 'Santa Catarina', 'value': 'SC'}
        ],
        value=['SP', 'SC'],
        multi=True
    ),

    html.Label('Radio Items'),
    dcc.RadioItems(
        options=[
            {'label': 'Rio Grande do Sul', 'value': 'NYC'},
            {'label': 'São Paulo', 'value': 'SP'},
            {'label': 'Santa Catarina', 'value': 'SC'}
        ],
        value='SP'
    ),

    html.Label('Checkboxes'),
    dcc.Checklist(
        options=[
            {'label': 'Rio Grande do Sul', 'value': 'NYC'},
            {'label': 'São Paulo', 'value': 'SP'},
            {'label': 'Santa Catarina', 'value': 'SC'}
        ],
        value=['SP', 'SC']
    ),

    html.Label('Text Input'),
    dcc.Input(value='SP', type='text'),

    html.Label('Slider'),
    dcc.Slider(
        min=0,
        max=9,
        marks={i: f'Label {i}' if i == 1 else str(i) for i in range(1, 6)},
        value=5,
    ),
], style={'columnCount': 2})
# ---- Start Server ---- #
if __name__ == '__main__':
    app.run_server(debug=True)