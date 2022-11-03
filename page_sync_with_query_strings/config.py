from dash import dcc

years = tuple(range(1000, 3000))

app_spanning_input = dcc.Dropdown(
    options=years,
    id="spanning-pages-year",
    persistence=True,
    persistence_type = 'memory',
)
app_spanning_input.initial = 2022