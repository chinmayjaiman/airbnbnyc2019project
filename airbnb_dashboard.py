import pandas as pd
import plotly.express as px
import dash
import dash_core_components as dcc
import dash_html_components as html

# Load the dataset and select only the first 1500 rows
df = pd.read_csv(r'C:\Users\chinm\Downloads\archive\AB_NYC_2019.csv', nrows= 1500)


# Create the app
app = dash.Dash(__name__)

# Define the layout of the app
app.layout = html.Div([
    # Title Charts 
    html.H1('Charts showing Airbnb Data of New York City for year 2019', style={'textAlign': 'center', 'fontFamily': 'Arial'}),


    # Summary statistics table
    html.Table(
    className='table table-bordered',
    style={'font-size': '1.1em', 
            # add border-collapse
           'border-collapse': 'collapse',
           # add a border
           'border': '1px solid black',  },
        children=[
        html.Thead(
            className='thead-dark',
            children=[
                html.Tr(
                    children=[
                        html.Th('Column'), html.Th('Mean'), html.Th('Standard Deviation'), html.Th('Minimum'), html.Th('Maximum')])
            ]
        ),
            html.Tbody(
            children=[
                html.Tr(
                    children=[
                        html.Td('price'), html.Td('{:.2f}'.format(df['price'].mean())), html.Td('{:.2f}'.format(df['price'].std())),  html.Td(df['price'].min()),  html.Td(df['price'].max())
                    ]
                ),
                    html.Tr(
                    children=[
                        html.Td('minimum_nights'), html.Td('{:.2f}'.format(df['minimum_nights'].mean())), html.Td('{:.2f}'.format(df['minimum_nights'].std())),  html.Td(df['minimum_nights'].min()), html.Td(df['minimum_nights'].max())
                    ]
                ),
                    html.Tr(
                        children=[
                            html.Td('number_of_reviews'), html.Td('{:.2f}'.format(df['number_of_reviews'].mean())), html.Td('{:.2f}'.format(df['number_of_reviews'].std())), html.Td(df['number_of_reviews'].min()), html.Td(df['number_of_reviews'].max())
                        ]
                    ),
                    html.Tr(
                        children=[
                            html.Td('reviews_per_month'), html.Td('{:.2f}'.format(df['reviews_per_month'].mean())), html.Td('{:.2f}'.format(df['reviews_per_month'].std())), html.Td(df['reviews_per_month'].min()),  html.Td(df['reviews_per_month'].max())
                        ]
                    ),
                    html.Tr(
                        children=[
                            html.Td('calculated_host_listings_count'),   html.Td('{:.2f}'.format(df['calculated_host_listings_count'].mean())), html.Td('{:.2f}'.format(df['calculated_host_listings_count'].std())), html.Td(df['calculated_host_listings_count'].min()),  html.Td(df['calculated_host_listings_count'].max())
                        ]
                    ),
                    html.Tr(
                        children=[
                            html.Td('availability_365'), html.Td('{:.2f}'.format(df['availability_365'].mean())), html.Td('{:.2f}'.format(df['availability_365'].std())), html.Td(df['availability_365'].min()), html.Td(df['availability_365'].max())])]
            )
        ]
    ),  
    # Histogram of price column
dcc.Graph(
    id='price-histogram',
    figure={
        'data': [
            {'x': df['price'], 'type': 'histogram', 'marker': {'color': 'navy'}, 'nbinsx': 30}
        ],
        'layout': {
            'title': 'Number of rooms available in various price brackets',
            'xaxis': {'title': 'Price', 'fixedrange': True},
            'yaxis': {'title': 'Number of rooms', 'fixedrange': True},
            'margin': {'l': 50, 'r': 50, 't': 50, 'b': 50},
            'plot_bgcolor': '#f8f9fa',
            'paper_bgcolor': '#f8f9fa',
        }
    },
    style={'height': '500px'}
    ),

   # Strip plot  of mean price by neighbourhood_group
    dcc.Graph(
    id='neighbourhood-group-strip',
    figure=px.strip(df, x='neighbourhood_group', y='price', title='Strip Plot of Price by Neighbourhood Group',
                    color='neighbourhood_group', hover_data=['neighbourhood']),
    style={'height': '500px', 'marginBottom': '50px'}
    ),
        
    # Horizontal stacked bar chart of the count of room types by neighbourhood
    dcc.Graph(
        id='room-type-by-neighbourhood',
        figure=px.bar(df, x='neighbourhood', color='room_type', barmode='stack', title='Count of Room Types by Neighbourhood',
                      color_discrete_sequence=px.colors.qualitative.Alphabet),
        style={'height': '500px', 'marginTop': '50px'}
    ),

    # Donut chart of room type distribution
    dcc.Graph(
    id='room-type-donut',
    figure=px.pie(df, values='price', names='room_type', hole=0.5, title='Room Type Distribution',
                 color_discrete_sequence=px.colors.qualitative.Alphabet),
    style={'width': '50%', 'height': '500px', 'marginTop': '50px', 'display': 'inline-block'}
    )
    ,

    # Pie chart of availability_365
    dcc.Graph(
        id='availability-pie',
        figure=px.pie(df, names='neighbourhood_group', values='availability_365', title='Pie Chart of Availability by Neighbourhood Group'),
        style={'width': '50%', 'height': '500px', 'marginTop': '50px', 'display': 'inline-block'}
        ),   

    # Scatter plot of price and minimum_nights with hover information
    dcc.Graph(
        id='price-minimum_nights-scatter',
                figure=px.scatter(df, x='price', y='minimum_nights', color='neighbourhood_group',
                      hover_data=['neighbourhood', 'room_type'], title='Scatter Plot of Price vs. Minimum Nights',
                      color_discrete_sequence=['#636EFA', '#EF553B', '#00CC96', '#AB63FA', '#FFA15A', '#19D3F3']),
                      style={'height': '500px', 'marginBottom': '50px'}
                      )                                                            

])


if __name__ == '__main__':
    app.run_server(debug=True)