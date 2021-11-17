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
dataFrame = pd.read_csv('tips.csv')

myFigure = px.scatter(x=dataFrame['total_bill'], y=dataFrame['tip'],
                      labels=dict(x="Total Bill Amount", y="Tip"),
                      title = 'Bill Amount and Tip')

# Display the scatterplot offline on your browser
myFigure.show()

