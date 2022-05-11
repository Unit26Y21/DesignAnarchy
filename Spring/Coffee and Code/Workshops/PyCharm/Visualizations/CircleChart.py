import plotly.express as px

df = px.data.gapminder().query("year == 2007").query("continent == 'Europe'")
df.loc[df['pop'] < 2.e6, 'country'] = 'Other countries' # Represent only large countries

print(df.to_string())

fig1 = px.pie(df, values='lifeExp', names='country', title='Life Expectancy of European continent')
fig2 = px.pie(df, values='gdpPercap', names='country', title='GPD of European continent')

fig1.show()
fig2.show()