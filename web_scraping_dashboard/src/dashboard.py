import dash
from dash import html, dcc
import plotly.express as px
import pandas as pd

app = dash.Dash(__name__)

df = pd.read_csv('../data/scraped_data.csv')

fig = px.bar(df, x='Column1', y='Column2')  # Replace with actual column names

app.layout = html.Div(children=[
    html.H1(children='Web Scraped Data Dashboard'),
    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)