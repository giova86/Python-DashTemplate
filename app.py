# index page
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State

from server import app, server
#from flask_login import logout_user, current_user

import pandas as pd
import plotly.express as px

# app pages
from pages import (
    home,
    page1,
    page2,
)

navbar = dbc.NavbarSimple(
    children=[
        dbc.NavItem(dbc.NavLink("Home", href="/home")),
        dbc.NavItem(dbc.NavLink("Page 1", href="/page1")),
        dbc.NavItem(dbc.NavLink("Page 2", href="/page2")),
    ],
    brand="Titolo NavBar",
    brand_href="/",
    color="primary",
    dark=True,
)

df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

app.layout = html.Div(
    [
        #header,
        navbar,
        html.Br(),
        html.Div(
            [
                dbc.Container(
                    id='page-content'
                )
            ]
        ),
        dcc.Location(id='base-url', refresh=False),
    ]
)


@app.callback(
    Output('page-content', 'children'),
    [Input('base-url', 'pathname')])
def router(pathname):
    '''
    routes to correct page based on pathname
    '''
    print('routing shit to',pathname)

    # app pages
    if pathname == '/' or pathname=='/home' or pathname=='/home':
        return home.layout()
    elif pathname == '/page1' or pathname=='/page1':
        return page1.layout()
    elif pathname == '/page2' or pathname=='/page2':
        return page2.layout()


if __name__ == '__main__':
    app.run_server(debug=True)
