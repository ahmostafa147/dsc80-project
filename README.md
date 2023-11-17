# League of Legends Having More kills Than Lane Oponnent Winrate Analysis

by Ahmed Mostafa and Ethan Vo (ahmostafa147, etvo@ucsd.edu)

---

## Introduction

Our dataset is on all of the professional League of Legends games that have taken place in 2023. The dataset contains 12 rows per game, one row per player and 2 rows of summary statistics (one for each team). Furthermore, there are over 100 columns of nearly all the data you could collect on a league of legends match. Our question is “Which player position, when achieving more kills than their lane opponent has the greatest impact on boosting the overall win rate?” Although the data does not explicitly collect information on whether a player has more kills than a lane opponent, we can collect the data from columns “kills”, “positions”, and “side”  to compare the kills of a player and their lane opponent and make our own column “has_more_kills.”

League of Legends players have always debated on which position needs kills to help the team win. As players continue to play League of Legends and try out the different positions on a team, players may get curious as to which position has the greatest influence on the game with more kills. Through this experiment they can know which position needs more kills than their lane opponent the most to help their team win.

The columns we are interested in to answer, “Which player position, when achieving more kills than their lane opponent has the greatest impact on boosting the overall win rate?” are: "gameid", "datacompleteness", "side", "position", "kills", "teamkills", “has_more_kills”, “result”, “league”, “killsat15” and “date”. We chose these columns because together they showed us from each game the kills from each position and whether or not they won. When we cleaned our data to only contain the information we needed to calculate win rates of each player with more kills than their lane opponents we had 11 columns, with our addition of “has_more_kills”, which we calculated, and 10772 rows.

Descriptions of Columns
* "result" is True when the team won the game and False otherwise
* “Kills” is the number of kills that particular player got in that game
* “gameid” is the identification number of the particular game from that tournament. This is unique for all games in the dataset
* “datacompleteness” is an indicator of whether or not the data is complete for that row
* “side” is the side that player played on. This can either be red or blue (corresponding to the red and blue sides on the map for League of Legends)
* “position” is the position or role the player played. This can be “top”, “mid”, “bot”, “jng”, or “sup” for the five positions in League of Legends.
* “kills” is the number of kills that the player got in the current game
* “teamkills” is the number of kills that the player’s team got in the particular game
* “has_more_kills” states whether or not the player has more kills than their lane opponent. It is a boolean that returns either “True” or “False”
* “result” is whether or not the team won. It will be 1 if the player’s team won or 0 for a loss.
* “league” is the professional league that the game is taking place in.
* “killsat15” is the number of kills a player got within the first 15 minutes of the particular game
* “date” is the date in which the particular game was played 

---

## Cleaning and EDA

We first decided to only keep the relevant columns: "gameid", "datacompleteness", "side", "position", "kills", "teamkills", “has_more_kills”, “result”, “league”, “killsat15” and “date” as they were relevant to our question. We cleaned the data by removing the rows that contain information about the team. We did this by removing the rows that had "team" value in the position column. We then added a new column to the DataFrame that identifies each row as whether it belongs to a position that had more kills than its counterpart in the opposing team. In order to create this column “has_more_kills”, we took the rows with the same “gameid” and “position” and compared the kills between the two sides. Our process is showed below:

```
lol_data = pd.read_csv('lol_data.csv', usecols=["gameid", "datacompleteness", "side", "position", "kills", "teamkills", "result"])
lol_data = lol_data.query("position != 'team'")
red = lol_data.sort_values(by=["gameid", "position"]).query("side == 'Red'")
blue = lol_data.sort_values(by=["gameid", "position"]).query("side == 'Blue'")
red["has_more_kills"] = np.array(red['kills']) > np.array(blue['kills'])
blue["has_more_kills"] = np.array(red['kills']) < np.array(blue['kills'])
col_added = red.merge(blue, how='outer').sort_values(by=["gameid", "position"])
```

This bar graph looks at the distribution of kills for each position. When result = 1, that player won the game. It appears that for the those who won games tend to have more kills than those who lost games. Support(sup) would normally defer kills to their teammates, and that is reflected as their distributions are closer to 0 than the other positions.

---

## Assessment of Missingness

Here's what a Markdown table looks like. Note that the code for this table was generated _automatically_ from a DataFrame, using

```py
print(counts[['Quarter', 'Count']].head().to_markdown(index=False))
```

| Quarter     |   Count |
|:------------|--------:|
| Fall 2020   |       3 |
| Winter 2021 |       2 |
| Spring 2021 |       6 |
| Summer 2021 |       4 |
| Fall 2021   |      55 |

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
Conclusion: We reject the null hypothesis. Meaning we believe that the proportion of winning and having more kills is less than winning and having less kills for supports.
Since we rejected the null hypothesis this means there is sufficient evidence that the proportion of support position winning and having higher kills is less than the proportion of support position winning and having less kills. We believe this means that supports having more kills is detrimental to the team winning the game.


---
