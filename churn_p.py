from plotly.offline import plot, iplot
import plotly.graph_objs as go
import numpy as np
import matplotlib as mpl
import plotly.plotly as py
from plotly.offline import init_notebook_mode
init_notebook_mode(connected=True)

x_negative = ["X8","X7","X6","X5"]
x_positive = ["X4","X3","X2","X1"]

y_negative = [16,45,16,20]
y_positive = [-16,-45,-5,-38]


trace_1 = go.Bar(y=x_negative, x=y_negative, name="<b>Negative</b>", 
											 orientation="h", 
											 marker=dict(color="#F6E3CE", line=dict(color='rgb(107,131,166)', width=1)))
trace_2 = go.Bar(y=x_positive, x=y_positive, name="<b>Positive</b>", 
											 orientation="h", 
											 marker=dict(color="#A9D0F5", line=dict(color='rgb(166,135,107)', width=1)))

layout_churn = dict(title="<b>Correlation with employees probability of churn</b>",
              yaxis=dict(title="<b>Variable</b>"))

data_churn = [trace_1,trace_2]
figure_churn = dict(data=data_churn, layout=layout_churn)
