import plotly.graph_objects as go
import json


fig = go.Figure(data = go.Bar(y=[2,3,1]))
fig.write_html('fig.html', auto_open=True)
