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

#break up data by the gender attribute
gk = dataFrame.groupby('gender')

#to find order of frequency for each gender
names_counts_F = gk.get_group('F')['race'].value_counts()
names_counts_M = gk.get_group('M')['race'].value_counts()

print(names_counts_F)
print(names_counts_M)


#labels in order of frequency
names = ['White, non-Hispanic', 'Black, non-Hispanic', 'Hispanic', 'Asian', 'Native American', 'Other']

#make two pie charts
myFigure = px.pie(values=gk.get_group('M')['race'].value_counts(),
                      names=names,
                      title = 'Proportion of Shootings by Race for Men')

myFigure1 = px.pie(values=gk.get_group('F')['race'].value_counts(),
                      names=names,
                      title = 'Proportion of Shootings by Race for Women')

# Display the scatterplot offline on your browser
myFigure.show()
myFigure1.show()

