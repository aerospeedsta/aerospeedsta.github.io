import plotly.graph_objects as go
import numpy as np
import os

# Create data directory if it doesn't exist
output_dir = "static/data"
os.makedirs(output_dir, exist_ok=True)

# Generate Torus data
u = np.linspace(0, 2*np.pi, 50)
v = np.linspace(0, 2*np.pi, 50)
u, v = np.meshgrid(u, v)

R = 3
r = 1

x = (R + r*np.cos(v)) * np.cos(u)
y = (R + r*np.cos(v)) * np.sin(u)
z = r * np.sin(v)

fig = go.Figure(data=[go.Surface(x=x, y=y, z=z)])

fig.update_layout(
    title='3D Torus',
    autosize=True,
    width=None,
    height=None,
    margin=dict(l=65, r=50, b=65, t=90)
)

# Export to JSON
# We save to static/data so it's accessible via /data/...
output_path = os.path.join(output_dir, "manifold_01.json")
fig.write_json(output_path)

print(f"Generated {output_path}")
