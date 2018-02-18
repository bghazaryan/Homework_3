import dash
import dash_core_components as dcc
import dash_html_components as html
import quandl
import pandas as pd
from plotly.offline import plot, iplot
import plotly.graph_objs as go
from plotly.offline import init_notebook_mode
init_notebook_mode(connected=True)

import churn_p
import gdp_p
import BC_GO_box_p
import BC_GO_table_p
import startup_chart_p

churn_graph = dcc.Graph(id="churn_p", figure=churn_p.figure_churn)
gdp_graph= dcc.Graph(id="gdp_p", figure=gdp_p.figure_gdp)
BC_GO_box = dcc.Graph(id="BC_GO_box_p", figure=BC_GO_box_p.graph_3)
BC_GO_table = dcc.Graph(id="BC_GO_table_p", figure=BC_GO_table_p.table_4)
startup_chart = dcc.Graph(id="startup_chart_p", figure=startup_chart_p.startup_chart)

app = dash.Dash()
app.css.append_css({'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'})

#creation and formating of Homework title

Homework_title = html.H1(children="Homework 3", style={'color': 'brown', 'text-align':'center', 'font-family': 'Comic Sans MS'})

#Graph titles

First_graph_title = html.H3(children="Graph 1")
Second_graph_title = html.H3(children="Graph 2")
Third_and_Forth_graph_title = html.H3(children="Graph 3 and 4")
Fifth_graph_title = html.H3(children="Graph 5")

#Graph descrition blocks

First_Graph_descriptive_block = html.P(children="The graph on the right hand side is showing correlations of different variables (call them from x1 to x8) with employee churn. Data is artificial, manually inputted by the developer. Recreate the graph. Small coloring or corelation value differences will be neglected.")
Second_Graph_descriptive_block = html.P(children="One the right hand side we have US GDP graphed over time. The data is sourced from QUANDL API (FRED/GDP). Your task is to recreate exactly the same graph.")
Third_and_Fourth_Graph_descriptive_block = html.P(children="The two graphs on this row are based on Google's stock (WIKI/GOOGL) and Bitcoin's (BCHARTS/ABUCOINSUSD) prices sourced from Quandl. First, percentage changes are calculated. Then the latter is plotted using Box plot to find the distribution and outliers. In the end the first 4 percentage changes (apart from the very first one, which is N/A) are plotted in a table. Recreate similar graphs with the same values (minor styling is neglected).")
Fifth_Graph_descriptive_block = html.P(children="Last graph is based on manually inputted data. It shows the Roadmap developed by an artificial startup. Task 1 is assumed to take the whole Janduary, while Task 2 is starting from March and ending in mid April. Afterwards, Task 3 begins and ends in the end of September. Recreate a similar Roadmap")


#Graph descritions width

First_graph_description = html.Div([
    First_graph_title, First_Graph_descriptive_block],
    className='four columns'
    )
Second_graph_description = html.Div([
    Second_graph_title, Second_Graph_descriptive_block],
    className='four columns'
    )
Third_and_Forth_graph_description = html.Div([
    Third_and_Forth_graph_title, Third_and_Fourth_Graph_descriptive_block],
    className='three columns'
    )
Fifth_graph_description = html.Div([
    Fifth_graph_title, Fifth_Graph_descriptive_block],
    className='four columns'
    )

#Width of colomn with graphs

First_graph_col = html.Div([
	churn_graph
    ],
    className='eight columns'
    )
Second_graph_col = html.Div([
	gdp_graph
    ],
    className='eight columns'
    )
Third_graph_col = html.Div([
	BC_GO_box
    ],
    className='four columns'
    )
Forth_graph_col = html.Div([
	BC_GO_table
    ],
    className='four columns'
    )
Fifth_graph_col = html.Div([
	startup_chart
    ],
    className='eight columns'
    )

#Divisions

First_graph_par_dev = html.Div([
    First_graph_description, First_graph_col],
    className='row'
    )
Second_graph_par_dev = html.Div([
    Second_graph_description, Second_graph_col],
    className='row'
    )
Third_and_Forth_graph_par_dev = html.Div([
    Third_and_Forth_graph_description, Third_graph_col, Forth_graph_col],
    className='row'
    )
Fifth_graph_par_dev =html.Div([
    Fifth_graph_description, Fifth_graph_col],
    className='row'
    )



#Container

container = html.Div([
	Homework_title,
	First_graph_par_dev,
	Second_graph_par_dev,
	Third_and_Forth_graph_par_dev,
	Fifth_graph_par_dev
	], className='row')

#Layout

app.layout = html.Div([
		container
	], className='row')

if __name__ == '__main__':
	app.run_server(debug=True)