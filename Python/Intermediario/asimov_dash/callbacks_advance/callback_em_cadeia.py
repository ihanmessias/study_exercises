import dash
from dash import html, dcc
from dash.dependencies import Input, Output

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

lista_de_cidades = {
    'Brasil': ['Rio de Janeiro', 'Minas Gerais', 'Paraná'],
    'Canada': [u'Montréal', 'Toronto', 'Ottawa']
}
app.layout = html.Div([
    dcc.RadioItems(
        id='countries-radio',
        options=[{f'label': k, 'value': k} for k in lista_de_cidades.keys()],
        value='Brasil'
    ),

    html.Hr(),
    dcc.RadioItems(id='cities-radio',),
    html.Hr(),
    html.Div(id='display-selected-values')
])


@app.callback(
    Output('cities-radio', 'options'),
    [Input('countries-radio', 'value')])
def set_cities_options(seleciona_cidade_value):
    return [{'label': i, 'value': i} for i in lista_de_cidades[seleciona_cidade_value]]


@app.callback(
    Output('cities-radio', 'value'),
    [Input('cities-radio', 'options')])
def set_cities_value(view_options):
    return view_options[0]['value']

# @app.callback(
#     Output(component_id='display-selected-value', component_property='children'),
#     [Input(component_id='countries-radio', component_property='value'),
#      Input(component_id='cities-radio', component_property='value')]
# )
# def update_output_div(value1, value2):
#     if value1 is None or value2 is None:
#         return 'Saída'
#     return f'Saída: {value1} {value2}'

@app.callback(
    Output('display-selected-values', 'children'),
    [Input('countries-radio', 'value'),
     Input('cities-radio', 'value')])
def set_display_children(seleciona_cidade_value, selected_city):
    return u'{} é uma cidade do {}'.format(
        selected_city, seleciona_cidade_value,
    )


if __name__ == '__main__':
    app.run_server(debug=True)