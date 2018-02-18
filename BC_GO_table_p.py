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
from plotly.offline import plot, iplot
import plotly.graph_objs as go
from plotly.offline import init_notebook_mode
init_notebook_mode(connected=True)

header_table_4 = dict(values=['Google', 'Bitcoin'],
                      align = ['left','center'],
              font = dict(color = 'white', size = 12),
              fill = dict(color='#119DFF')
                         )
             
cells_table_4 = dict(values=[round(google_data.Open.pct_change().head()[1:],3),
                              round(bitcoin_data.Open.pct_change().head()[1:],3)],
             align = ['left','center'],
             fill = dict(color=["yellow","white"])
            )
trace_table_4 = go.Table(header=header_table_4, cells=cells_table_4)

data_table_4 = [trace_table_4]
layout_table_4 = dict(width=500, height=300)
table_4 = dict(data=data_table_4, layout=layout_table_4)
