import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px

# Sample data (you can replace this with your actual data)
data = pd.read_csv('formatted_merged_output.csv')

# Create a Dash application
app = dash.Dash(__name__)

# Define the layout of the app
app.layout = html.Div([
    html.H1("Soul Foods Sales Visualization"),
    
    # Dropdown for selecting the date
    dcc.Dropdown(
        id='date-dropdown',
        options=[{'label': date, 'value': date} for date in data['Date'].unique()],
        value=data['Date'].max(),  # Default to the latest date
        multi=False
    ),

    # Line chart to visualize sales data
    dcc.Graph(id='sales-chart')
])

# Define callback to update the line chart based on selected date
@app.callback(
    dash.dependencies.Output('sales-chart', 'figure'),
    [dash.dependencies.Input('date-dropdown', 'value')]
)
def update_sales_chart(selected_date):
    filtered_data = data[data['Date'] == selected_date]

    # Create a line chart
    fig = px.line(filtered_data, x='Date', y='Sales', title='Sales Over Time')
    fig.update_xaxes(title='Date')
    fig.update_yaxes(title='Sales')

    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
