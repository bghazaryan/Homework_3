import pandas as pd
from plotly.offline import plot, iplot
import plotly.graph_objs as go
from plotly.offline import init_notebook_mode
init_notebook_mode(connected=True)

import quandl
quandl.ApiConfig.api_key = "HyaKYY8tnWQAgPyX36rL"



google_data = quandl.get("WIKI/GOOGL")
google_data.head()
bitcoin_data = quandl.get("BCHARTS/ABUCOINSUSD")
bitcoin_data.head()
percentage_change_bitcoin = go.Box(x=bitcoin_data.Open.pct_change(), name="<b>Bitcoin</b>")
percentage_change_google = go.Box(x=google_data.Open.pct_change(), name="<b>Google</b>")

layout_grapth_3 = dict(title="<i>Distribution of Price</i>")

data_graph_3 = [percentage_change_bitcoin, percentage_change_google]
graph_3 = dict(data=data_graph_3, layout=layout_grapth_3)

