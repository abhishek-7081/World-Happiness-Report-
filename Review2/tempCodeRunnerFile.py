# GDP vs Happiness (interactive)
fig = px.scatter(happy_df,
                 x='Logged GDP per capita',
                 y='Happiness score',
                 color='Regional indicator',
                 hover_name='Country name',
                 title='GDP per Capita vs Happiness Score (Interactive)')
fig.write_html('Visualizations/gdp_vs_happiness_plotly.html', include_plotlyjs='cdn')
fig.show()