import dash
from dash import dcc, html
from dash import Output, Input, State, callback

import config

dash.register_page(__name__, path="/page3")

def layout(year=None, **other_unknown_query_strings):
    print(year,hasattr(config.app_spanning_input, 'value')) # line for debug purposes
    if year is None:
        config.app_spanning_input.value = config.app_spanning_input.initial
    elif type(year) is str: # a string value has been passed through a query string in URL
        config.app_spanning_input.value = int(year) if (all(c in '0123456789' for c in year) and int(year) in config.years) else None # make sure the query string value can be interpreted as an integer and it is in the options range
    return html.Div(
    [
        html.Label("Page 3 Select Year"),
        config.app_spanning_input,
        html.Div(id="page3-out"),
    ]
)


@callback(
    Output("page3-out", "children"),
    Input("spanning-pages-year", "value")
    )
def update(year):
    return f"The dropdown is {year}"
