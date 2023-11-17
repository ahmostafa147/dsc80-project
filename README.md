# League of Legends Having More kills Than Lane Oponnent Winrate Analysis

by Ahmed Mostafa and Ethan Vo (ahmostafa@ucsd.edu, etvo@ucsd.edu)

---

## Introduction

Our dataset is on all of the professional League of Legends games that have taken place in 2023. The dataset contains 12 rows per game, one row per player and 2 rows of summary statistics (one for each team). Furthermore, there are over 100 columns of nearly all the data you could collect on a league of legends match. Our question is “Which player position, when achieving more kills than their lane opponent has the greatest impact on boosting the overall win rate?” Although the data does not explicitly collect information on whether a player has more kills than a lane opponent, we can collect the data from columns “kills”, “positions”, and “side”  to compare the kills of a player and their lane opponent and make our own column “has_more_kills.”

League of Legends players have always debated on which position needs kills to help the team win. As players continue to play League of Legends and try out the different positions on a team, players may get curious as to which position has the greatest influence on the game with more kills. Through this experiment they can know which position needs more kills than their lane opponent the most to help their team win.

The columns we are interested in to answer, “Which player position, when achieving more kills than their lane opponent has the greatest impact on boosting the overall win rate?” are: <code class="language-plaintext highlighter-rouge">“gameid”</code>, <code class="language-plaintext highlighter-rouge">“datacompleteness”</code>, <code class="language-plaintext highlighter-rouge">“side”</code>, <code class="language-plaintext highlighter-rouge">“position”</code>, <code class="language-plaintext highlighter-rouge">“kills”</code>, <code class="language-plaintext highlighter-rouge">“teamkills”</code>, <code class="language-plaintext highlighter-rouge">“has_more_kills”</code>, <code class="language-plaintext highlighter-rouge">“result”</code>, <code class="language-plaintext highlighter-rouge">“league”</code>, <code class="language-plaintext highlighter-rouge">“killsat15”</code> and <code class="language-plaintext highlighter-rouge">“date”</code>. We chose these columns because together they showed us from each game the kills from each position and whether or not they won. When we cleaned our data to only contain the information we needed to calculate win rates of each player with more kills than their lane opponents we had 11 columns, with our addition of “has_more_kills”, which we calculated, and 10772 rows.

Descriptions of Columns

* <code class="language-plaintext highlighter-rouge">"result"</code> is True when the team won the game and False otherwise
* <code class="language-plaintext highlighter-rouge">"kills"</code> is the number of kills that particular player got in that game
* <code class="language-plaintext highlighter-rouge">"gameid"</code> is the identification number of the particular game from that tournament. This is unique for all games in the dataset
* <code class="language-plaintext highlighter-rouge">"datacompleteness"</code> is an indicator of whether or not the data is complete for that row
* <code class="language-plaintext highlighter-rouge">"side"</code> is the side that player played on. This can either be red or blue (corresponding to the red and blue sides on the map for League of Legends)
* <code class="language-plaintext highlighter-rouge">“position”</code> is the position or role the player played. This can be “top”, “mid”, “bot”, “jng”, or “sup” for the five positions in League of Legends.
* <code class="language-plaintext highlighter-rouge">“kills”</code> is the number of kills that the player got in the current game
* <code class="language-plaintext highlighter-rouge">“teamkills”</code> is the number of kills that the player’s team got in the particular game
* <code class="language-plaintext highlighter-rouge">“has_more_kills”</code> states whether or not the player has more kills than their lane opponent. It is a boolean that returns either “True” or “False”
* <code class="language-plaintext highlighter-rouge">“result”</code> is whether or not the team won. It will be 1 if the player’s team won or 0 for a loss.
* <code class="language-plaintext highlighter-rouge">“league”</code> is the professional league that the game is taking place in.
* <code class="language-plaintext highlighter-rouge">“killsat15”</code> is the number of kills a player got within the first 15 minutes of the particular game
* <code class="language-plaintext highlighter-rouge">“date”</code> is the date in which the particular game was played 

---

## Data Cleaning and Exploratory Data Analysis

We first decided to only keep the relevant columns: <code class="language-plaintext highlighter-rouge">“gameid”</code>, <code class="language-plaintext highlighter-rouge">“datacompleteness”</code>, <code class="language-plaintext highlighter-rouge">“side”</code>, <code class="language-plaintext highlighter-rouge">“position”</code>, <code class="language-plaintext highlighter-rouge">“kills”</code>, <code class="language-plaintext highlighter-rouge">“teamkills”</code>, <code class="language-plaintext highlighter-rouge">“has_more_kills”</code>, <code class="language-plaintext highlighter-rouge">“result”</code>, <code class="language-plaintext highlighter-rouge">“league”</code>, <code class="language-plaintext highlighter-rouge">“killsat15”</code> and <code class="language-plaintext highlighter-rouge">“date”</code> as they were relevant to our question. We cleaned the data by removing the rows that contain information about the team. We did this by removing the rows that had "team" value in the position column. We then added a new column to the DataFrame that identifies each row as whether it belongs to a position that had more kills than its counterpart in the opposing team. In order to create this column <code class="language-plaintext highlighter-rouge">“has_more_kills”</code>, we took the rows with the same <code class="language-plaintext highlighter-rouge">“gameid”</code> and <code class="language-plaintext highlighter-rouge">“position”</code> and compared the kills between the two sides. Our process is showed below:

```py
import pandas as pd
import numpy as np
lol_data = pd.read_csv('lol_data.csv', usecols=["gameid", "datacompleteness", "side", "position", "kills", "teamkills", "result"])
lol_data = lol_data.query("position != 'team'")
red = lol_data.sort_values(by=["gameid", "position"]).query("side == 'Red'")
blue = lol_data.sort_values(by=["gameid", "position"]).query("side == 'Blue'")
red["has_more_kills"] = np.array(red['kills']) > np.array(blue['kills'])
blue["has_more_kills"] = np.array(red['kills']) < np.array(blue['kills'])
col_added = red.merge(blue, how='outer').sort_values(by=["gameid", "position"])
print(col_added.head().to_markdown(index=False))
```

Univariate Charts


```py
more_kills_won = (col_added
                  .query("result == 1 and has_more_kills == True")
                  .shape[0] / 
                  col_added
                  .query("has_more_kills == True")
                  .shape[0]
                 )
more_kills_lost = 1 - more_kills_won
data = {'rate': [more_kills_won, more_kills_lost],
        'Label': ['Had more kills and won', 'Had more kills but lost']}
df = pd.DataFrame(data)
fig = px.pie(df, values='rate', names='Label', title='Players winning rate when having more kills')
fig.show()
```
<iframe src="univariate_chart1.py" width=800 height=600 frameBorder=0></iframe>

In order to increase our awareness of the data we have, we produced an interactive pie chart using plotly that reprensents the percentage of players who had more kills and won vs players who had more kills but won. This visualization is helpful to give us insight of what to expect from our proportions that represents the impact of having more kills. As we can see, 79.4% of the players who had more kills won. This gives us insight about what our proportions would look like per position. It makes us expect that having more kills should have a big impact on your chances of winning.

```py
fig = (px.histogram(lol_data,
                    x="kills",
                    facet_col= "position",
                    facet_row = "result",
                    title="Kills Distribution Per Position",
                    histnorm="probability density")
      )
fig.show()
```

This histogram shows the distribution of kills counts per position for winning vs losing players. Generally winning players had more kills than losing players.

Bivariate Chart

```py
prop_per_position_more = (col_added
                     .query("has_more_kills == True and result == 1")
                     .groupby("position")
                     .size() / 
                     col_added
                     .groupby('position')
                     .size()
                    )
prop_per_position_more.name = "Proportions"
fig2 = px.bar(prop_per_position_more, title="Win Rate of Position with more Kills")
fig2.update_layout(
    legend=dict(title='Variable'),  # Add legend title
    yaxis_title='Win Rate', # Add y-axis label
)
fig2.show()
```

This bar graph looks at the distribution of kills for each position. When result = 1, that player won the game. It appears that for the those who won games tend to have more kills than those who lost games. Support(<code class="language-plaintext highlighter-rouge">“sup”</code>) would normally defer kills to their teammates, and that is reflected as their distributions are closer to 0 than the other positions.

```py
prop_per_position_less = (col_added
                          .query("has_more_kills == False and result == 1")
                          .groupby("position")
                          .size() / 
                          col_added
                          .groupby('position')
                          .size()
                         )
observed_stat = (prop_per_position_more - prop_per_position_less)
observed_stat.name = "Proportions"
fig2 = px.bar(observed_stat, title="Increase in Win Rate of Position With More Kills vs Less Kills")
fig2.update_layout(
    legend=dict(title='Variable'),  # Add legend title
    yaxis_title='Win Rate', # Add y-axis label
)
fig2.show()
```

This bar graph shows the difference in winrate when having more kills than their lane opponent versus having less kills than their lane opponenet. One thing intriguing is that the support role is the only role that had a negative difference in winrate, which we would further invesitgate in our hypothesis testing.

---

## Assessment of Missingness

NMAR Analysis
Yes, we believe that many columns in our data are Not Missing At Random (NMAR) due to the way this data is collected. Each game has 12 rows: two sets of 5 rows for each of the team players and an additional row for each team’s summary statistics. Many stats are missing for the player rows and not missing for the team rows, and vice versa. This makes the missingness of the rows dependent on the type of columns (and therefore many of the other columns). However, this missingness is not missing by design because we cannot always infer one column’s missingness exactly from another in the columns that we had. 

Furthermore, special individual statistics were recorded differently based on the league the game took place in. It appeared that some leagues did not record the individual kill statistics in rows for the players and not the teams. <code class="language-plaintext highlighter-rouge">“killsat15”</code>, one of the individual kill statistics, we speculate will have its missingness dependent on the <code class="language-plaintext highlighter-rouge">“league”</code> column based on this fact.

The data we had in our hypothesis testing did not have any rows without values. <code class="language-plaintext highlighter-rouge">“kills”</code> were recorded in every single game for every single individual in the dataset, so we did not need to impute any data in order to complete the data for our hypothesis testing.

---

## Hypothesis Testing

**Null Hypothesis**: The proportion of **support** position winning and having higher kills is equal to the proportion of support position winning and having less kills.
**Alternative Hypothesis**: The proportion of **support** position winning and having higher kills is less than the proportion of support position winning and having less kills.
Test Statistic: We will be using the proportion of games won.
* We chose to use proportions because we are looking at has_more_kills influence on the winrate of a player.
Significance Level: 5% (0.05)
* We chose this significance level because it is the standard
p-value: 0
* We did 10,000 simulations

Conclusion: Since the p value is 0, we reject the null hypothesis. Our observations is not consistent with the hypothesis that the change in win rate for supports with more kills than their lane opponents is less than 0. We believe this means that supports having more kills may be detrimental to the team winning the game.


---
