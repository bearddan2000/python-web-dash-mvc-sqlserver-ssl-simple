import dash
from dash import html, dash_table
import pandas as pd
from sqlalchemy import create_engine

import settings

# engine = create_engine('sqlite:///:memory:', echo=True)
engine = create_engine(
    '{engine}://{username}:{password}@{host}/{db_name}'.format(
        **settings.SQLSERVER
    ),
    echo=settings.SQLALCHEMY['debug']
)

dataframe = pd.read_sql_query('SELECT id, breed, color FROM dog', engine )

app = dash.Dash()

app.layout = html.Div([
    html.H1([
        "Dog Table"
    ]),
    dash_table.DataTable(
        data=dataframe.to_dict('records'),
        columns=[{'id': c, 'name': c, 'name': c} for c in dataframe.columns],
        fill_width=False,
        style_cell_conditional=[
            {
                'if': {'column_id': c},
                'textAlign': 'left'
            } for c in ['name', 'color']
        ],
        style_data={
            'color': 'black',
            'backgroundColor': 'white'
        },
        style_data_conditional=[
            {
                'if': {'row_index': 'odd'},
                'backgroundColor': 'rgb(220, 220, 220)',
            }
        ],
        style_header={
            'backgroundColor': 'rgb(210, 210, 210)',
            'color': 'black',
            'fontWeight': 'bold',
            'fontSize': 18,
            'text-transform': 'capitalize',
            'textAlign': 'center'
        },
        style_cell={
            'border': 'thin solid #000000'
        }
    )
])

if __name__ == '__main__':
    app.run_server(host='0.0.0.0', debug=True)
