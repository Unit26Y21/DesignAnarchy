import plotly.graph_objects as go

fig = go.Figure(data=[go.Sankey(
    node = dict(
      pad = 15,
      thickness = 20,
      line = dict(color = "black", width = 0.5),
      label = ["Air Rights Sold",
               "Air Rights Developed",
               "Sold Open Market",
               "Sold Reparative Market",
               "Revenue from Air Rights Sale",
               "Revenue from Air Rights Developed"],
      color = "blue"
    ),
    link = dict(
      source = [0, 0, 1, 2, 3], # indices correspond to labels, eg A1, A2, A1, B1, ...
      target = [2, 3, 5, 4, 4],
      value = [90, 20, 30, 10, 40, 100]
  ))])

print(fig.go)
fig.update_layout(title_text="Basic Sankey Diagram", font_size=16)

fig.show()