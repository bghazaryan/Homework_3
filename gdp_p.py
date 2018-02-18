import quandl
import pandas as pd
import plotly
from plotly.offline import plot, iplot
import plotly.graph_objs as go
from plotly.offline import init_notebook_mode
init_notebook_mode(connected=True)

quandl.ApiConfig.api_key = "HyaKYY8tnWQAgPyX36rL"

data1 = quandl.get("FRED/GDP")
data1.head()

x_values_2 = data1.index
y_values_2 = data1["Value"]
trace_2 = go.Scatter(x=x_values_2,y=y_values_2,mode="lines", fill='tonexty')

layout_1 = dict(title="<b>US GDP over time</b>")

gdp_data = [trace_2]
figure_gdp = dict(data=gdp_data, layout=layout_1)
