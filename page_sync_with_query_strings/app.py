"""
 This example demonstrates syncing input components between pages of a multi-page app using persistence.
"""

import dash
from dash import html,dcc

import dash_bootstrap_components as dbc

app = dash.Dash(
    __name__,
    use_pages=True,
    # prevent_initial_callbacks=True,
    # suppress_callback_exceptions=True,
    external_stylesheets=[dbc.themes.BOOTSTRAP],
)

dash.register_page("home", layout=html.H4("This is the home page, go to any page to set year."), path="/")

app.layout = dbc.Container(
    [
        html.H1("Multi Page App Demo: Sync components between pages"),
        html.Div(
            [
                html.Div(
                    dcc.Link(f"{page['name']}", href=page["path"]),
                )
                for page in dash.page_registry.values()
            ]
        ),
        html.Hr(),
        dash.page_container,
    ],
    fluid=True,
)


if __name__ == "__main__":
    app.run_server(debug=True)
