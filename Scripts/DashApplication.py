import dash
from dash import dcc, html, Input, Output
import pandas as pd
import plotly.express as px

# Sample data (you can replace this with your actual data)
data = pd.read_csv('formatted_merged_output.csv')

# Create a Dash application
app = dash.Dash(__name__)

# Define the layout of the app with CSS styling
app.layout = html.Div([
    html.Div([
        html.H1("Soul Foods Sales Visualization", style={'text-align': 'center', 'font-size': '24px'}),
        
        dcc.RadioItems(
            id='region-radio',
            options=[
                {'label': 'North', 'value': 'north'},
                {'label': 'East', 'value': 'east'},
                {'label': 'South', 'value': 'south'},
                {'label': 'West', 'value': 'west'},
                {'label': 'All', 'value': 'all'},
            ],
            value='all',  # Default to showing data for all regions
            labelStyle={'display': 'block', 'font-size': '18px'},
            style={'text-align': 'center', 'margin-top': '20px'}
        ),

        dcc.Graph(id='sales-chart'),

    ], style={'width': '80%', 'margin': '0 auto'}),
], style={'background-color': '#f4f4f4', 'padding': '20px'})

# Define callback to update the line chart based on selected region
@app.callback(
    Output('sales-chart', 'figure'),
    [Input('region-radio', 'value')]
)
def update_sales_chart(selected_region):
    if selected_region == 'all':
        filtered_data = data[data['Date'] == data['Date'].max()]  # Show all regions for the selected date
    else:
        filtered_data = data[(data['Date'] == data['Date'].max()) & (data['Region'] == selected_region)]

    # Create a line chart
    fig = px.line(filtered_data, x='Date', y='Sales', title='Sales Over Time', labels={'Date': 'Date', 'Sales': 'Sales'})
    fig.update_xaxes(title_text='')
    fig.update_yaxes(title_text='')

    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
