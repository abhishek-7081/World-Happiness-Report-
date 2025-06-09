# Import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import warnings
warnings.filterwarnings("ignore")

# Load dataset
df = pd.read_csv('Dataset/whr2023.csv')

# Filter columns for analysis
columns = ['Country name', 'iso alpha', 'Regional indicator', 'Happiness score',
           'Logged GDP per capita', 'Social support', 'Healthy life expectancy',
           'Freedom to make life choices', 'Generosity', 'Perceptions of corruption']
happy_df = df[columns].copy()

# Top 10 happiest countries
top10 = happy_df.sort_values(by='Happiness score', ascending=False).head(10)
plt.figure(figsize=(10,6))
sns.barplot(data=top10, y='Country name', x='Happiness score', palette='viridis')
plt.title('Top 10 Happiest Countries (2023)')
plt.tight_layout()
plt.savefig('Visualizations/top10_happiness_bar.png')
plt.show()

# Correlation heatmap
plt.figure(figsize=(10,8))
sns.heatmap(happy_df.drop(['Country name', 'iso alpha', 'Regional indicator'], axis=1).corr(),
            annot=True, cmap='coolwarm')
plt.title('Correlation Heatmap of Happiness Factors')
plt.tight_layout()
plt.savefig('Visualizations/heatmap_corr.png')
plt.show()

# GDP vs Happiness (interactive)
fig = px.scatter(happy_df,
                 x='Logged GDP per capita',
                 y='Happiness score',
                 color='Regional indicator',
                 hover_name='Country name',
                 title='GDP per Capita vs Happiness Score (Interactive)')
fig.write_html('Visualizations/gdp_vs_happiness_plotly.html', include_plotlyjs='cdn')
fig.show()
