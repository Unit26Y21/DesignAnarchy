import plotly.express as px
import pandas as pd

df = px.data.wind()

df = pd.DataFrame()

print(df.to_string())

fig = px.line_polar(df, r="frequency", theta="direction", color="strength", line_close=True,
                    color_discrete_sequence=px.colors.sequential.deep,
                    template="plotly_dark",)
fig.show()