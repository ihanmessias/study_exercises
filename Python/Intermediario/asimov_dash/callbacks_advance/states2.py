from dash import Dash, dcc, html
from dash.dependencies import Input, Output, State

app = Dash(__name__)

app.layout = html.Div([
    dcc.Input(id='input-1-state', type='text', value='Montréal'),
    dcc.Input(id='input-2-state', type='text', value='Canada'),
    html.Button(id='submit-button-state', children='Submit'),
    html.Div(id='output-state')
])


@app.callback(Output(component_id='output-state', component_property='children'),
            Input(component_id='submit-button-state', component_property='n_clicks'),
            State('input-1-state', 'value'),
            State('input-2-state', 'value')
)
def update_output(n_clicks, input1, input2):
    return u'Input 1 is "{}",and Input 2 is "{}"'.format(input1, input2)


if __name__ == '__main__':
    app.run_server(debug=True)