import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd


df = pd.read_csv('amazon.csv')

state_options = df["state"].unique()

app = dash.Dash()

app.layout = html.Div([
    html.H2("Amazon forest fire"),
    html.Div(
        [
            dcc.Dropdown(
                id="state",
                options=[{
                    'label': i,
                    'value': i
                } for i in state_options],
                value='state'),
        ],
        style={'width': '25%',
               'display': 'inline-block'}),
    dcc.Graph(id='funnel-graph'),
])


@app.callback(
    dash.dependencies.Output('funnel-graph', 'figure'),
    [dash.dependencies.Input('state', 'value')])
def update_graph(state):
    if state == "All state":
        df_plot = df.copy()
    else:
        df_plot = df[df['state'] == state]

    pv = pd.pivot_table(
        df_plot,
        index=['year'],
        columns=["month"],
        values=['number'],
        aggfunc=sum,
        fill_value=0)

    trace1 = go.Bar(x=pv.index, y=pv[('number', 'Janeiro')], name='January')
    trace2 = go.Bar(x=pv.index, y=pv[('number', 'Fevereiro')], name='Febuary')
    trace3 = go.Bar(x=pv.index, y=pv[('number', 'Março')], name='March')
    trace4 = go.Bar(x=pv.index, y=pv[('number', 'Abril')], name='April')
    trace5 = go.Bar(x=pv.index, y=pv[('number', 'Maio')], name='May')
    trace6 = go.Bar(x=pv.index, y=pv[('number', 'Junho')], name='June')
    trace7 = go.Bar(x=pv.index, y=pv[('number', 'Julho')], name='July')
    trace8 = go.Bar(x=pv.index, y=pv[('number', 'Agosto')], name='August')
    trace9 = go.Bar(x=pv.index, y=pv[('number', 'Setembro')], name='September')
    trace10 = go.Bar(x=pv.index, y=pv[('number', 'Outubro')], name='October')
    trace11 = go.Bar(x=pv.index, y=pv[('number', 'Novembro')], name='November')
    trace12 = go.Bar(x=pv.index, y=pv[('number', 'Dezembro')], name='December')



    return {
        'data': [trace1, trace2, trace3, trace4,trace5, trace6, trace7, trace8,trace9, trace10, trace11, trace12],
        'layout':
        go.Layout(
            title='Forest fires for {}'.format(state),
            barmode='stack')
    }


if __name__ == '__main__':
     app.run_server(debug=True,port= '2341')