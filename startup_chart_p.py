import pandas as pd
from plotly.offline import plot, iplot
import plotly.graph_objs as go
from plotly.offline import init_notebook_mode
init_notebook_mode(connected=True)

import plotly.plotly as py
import plotly.figure_factory as ff

df = [dict(Task="Task 1", Start='2018-01-01', Finish='2018-01-31', Resource='Idea Validation'),
      dict(Task="Task 2", Start='2018-03-01', Finish='2018-04-16', Resource='Prototyping'),
      dict(Task="Task 3", Start='2018-04-17', Finish='2018-09-30', Resource='Team Formation')]

colors = ['#f79204', (0.2, 0.7, 0.3), 'rgb(6, 22, 137)']

startup_chart = ff.create_gantt(df, colors=colors, index_col='Resource', reverse_colors=True, show_colorbar=True, title="Startup Roadmap")
