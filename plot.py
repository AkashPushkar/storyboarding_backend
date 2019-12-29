import plotly.graph_objects as go
import json

file = "./data/panoptic_coco_categories.json"
with open(file, 'r') as file:
    data = json.load(file)

r = []
g = []
b = []
for d in data:
    r.append(d['color'][0])
    g.append(d['color'][1])
    b.append(d['color'][2])


fig = go.Figure(data = [go.Scatter3d(x=r, y=g, z=b,
                            mode='markers',
                            marker=dict(size=12,color=b, colorscale='Viridis',opacity=0.8)
                    )])
fig.show()
