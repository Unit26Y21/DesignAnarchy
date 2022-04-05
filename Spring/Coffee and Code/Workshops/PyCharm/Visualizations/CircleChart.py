import plotly.express as px

df = px.data.gapminder().query("year == 2007").query("continent == 'Europe'")
df.loc[df['pop'] < 2.e6, 'country'] = 'Other countries' # Represent only large countries

print(df)

fig = px.pie(df, values='gdpPercap', names='country', title='Population of European continent')
fig.show()