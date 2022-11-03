from dash import dcc, html
from dash import Output, Input, State, callback

import dash
import config

dash.register_page(__name__, path="/page1")

layout = html.Div(
    [
        html.Label("Page 1 Select Year"),
        config.app_spanning_input,
        html.Div(id="page1-out"),
    ]
)

@callback(
    Output("page1-out", "children"),
    Input("all-pages-year", "value")
    )
def update(year):
    return f"The dropdown is {year}"
