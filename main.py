#### Get all the installations from https://plotly.com/python/getting-started/
### Nice practice - https://plot.ly/python/creating-and-updating-figures/
import plotly
import pandas as pd
import plotly.graph_objs as go
import plotly.express as px
import plotly.io as pio

# Change default renderer to browser so that your figures can show up in your browser
pio.renderers.default = "browser"

# Setup dataframe
dataFrame = pd.read_csv('shootings-data.csv')

gk = dataFrame.groupby('gender')

#print(gk.first())

names = ['White, non-Hispanic', 'Black, non-Hispanic', 'Hispanic', 'Asian', 'Native American', 'Other']

myFigure = px.pie(values=gk.get_group('M')['race'].value_counts(),
                      names=names,
                      title = 'Proportion of shootings by race for men')

myFigure1 = px.pie(values=gk.get_group('F')['race'].value_counts(),
                      names=names,
                      title = 'Proportion of shootings by race for women')

# Display the scatterplot offline on your browser
myFigure.show()
myFigure1.show()

