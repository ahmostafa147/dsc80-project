import pandas as pd
import numpy as np
import plotly.express as px

# Calculate rates for more kills won and lost
more_kills_won = (col_added.query("result == 1 and has_more_kills == True").shape[0] / col_added.query("has_more_kills == True").shape[0])
more_kills_lost = 1 - more_kills_won

# Create a DataFrame for the pie chart
data = {'rate': [more_kills_won, more_kills_lost],
        'Label': ['Had more kills and won', 'Had more kills but lost']}
df = pd.DataFrame(data)

# Generate pie chart using Plotly
fig = px.pie(df, values='rate', names='Label', title='Players winning rate when having more kills')

# Save the Plotly figure as an HTML file
fig.write_html("plot.html")

with open("chart.html") as f:
  chart_html = f.read()
