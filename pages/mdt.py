import dash
from dash import html

dash.register_page(__name__)

layout = html.Div([
    html.H1('This is our MDT page'),
    html.Div('This is our MDT page content.'),
])