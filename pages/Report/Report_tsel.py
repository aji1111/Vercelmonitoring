import dash
from dash import html

dash.register_page(__name__)

layout = html.Div([
    html.H1('Report to Tsel'),
    html.Div('This is our Report to Tsel'),
])