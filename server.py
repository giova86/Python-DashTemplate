# Dash app initialization
import dash
import dash_bootstrap_components as dbc

# global imports
import os
import random

app = dash.Dash(
    __name__,
    update_title=None,
    external_stylesheets=[dbc.themes.BOOTSTRAP]
)

server = app.server
app.config.suppress_callback_exceptions = True
app.title = 'Dash Template'
