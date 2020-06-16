import pandas as pd

data = pd.read_csv('data/gapminder_gdp_oceania.csv', index_col='country')
years = data.columns.str.strip('gdpPercap_')
data.columns = years.astype(int)
