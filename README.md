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

| gameid             | datacompleteness   | league   | side   | position   |   result |   kills |   teamkills |   killsat15 | has_more_kills   |
|:-------------------|:-------------------|:---------|:-------|:-----------|---------:|--------:|------------:|------------:|:-----------------|
| 10000-10000_game_1 | partial            | LDL      | Red    | bot        |        1 |      11 |          21 |         nan | True             |
| 10000-10000_game_1 | partial            | LDL      | Blue   | bot        |        0 |       3 |           4 |         nan | False            |
| 10000-10000_game_1 | partial            | LDL      | Red    | jng        |        1 |       7 |          21 |         nan | True             |
| 10000-10000_game_1 | partial            | LDL      | Blue   | jng        |        0 |       0 |           4 |         nan | False            |
| 10000-10000_game_1 | partial            | LDL      | Red    | mid        |        1 |       2 |          21 |         nan | True             |

Univariate Charts

<iframe src="assets/piechart.html" width="800" height="600" frameBorder="0"></iframe>

In order to increase our awareness of the data we have, we produced an interactive pie chart using plotly that reprensents the percentage of players who had more kills and won vs players who had more kills but won. This visualization is helpful to give us insight of what to expect from our proportions that represents the impact of having more kills. As we can see, 79.4% of the players who had more kills won. This gives us insight about what our proportions would look like per position. It makes us expect that having more kills should have a big impact on your chances of winning.

<iframe src="assets/histogram_distribution.html" width="800" height="600" frameBorder="0"></iframe>

This histogram shows the distribution of kills counts per position for winning vs losing players. Generally winning players had more kills than losing players.

Bivariate Chart

<iframe src="assets/more_kills_barchart.html" width="800" height="600" frameBorder="0"></iframe>

This bar graph looks at the distribution of kills for each position. When result = 1, that player won the game. It appears that for the those who won games tend to have more kills than those who lost games. Support(<code class="language-plaintext highlighter-rouge">“sup”</code>) would normally defer kills to their teammates, and that is reflected as their distributions are closer to 0 than the other positions.

<iframe src="assets/increase_win_rate_barchart.html" width="800" height="600" frameBorder="0"></iframe>

This bar graph shows the difference in winrate when having more kills than their lane opponent versus having less kills than their lane opponenet. One thing intriguing is that the support role is the only role that had a negative difference in winrate, which we would further invesitgate in our hypothesis testing.

Interesting Aggregates

|   result |     bot |     jng |     mid |     sup |     top |
|---------:|--------:|--------:|--------:|--------:|--------:|
|        0 | 2.72391 | 1.80124 | 2.27191 | 0.58225 | 1.70358 |
|        1 | 6.27757 | 3.46807 | 4.85156 | 1.01652 | 3.5129  |

---

## Assessment of Missingness

NMAR Analysis
Yes, we believe that many columns in our data are Not Missing At Random (NMAR) due to the way this data is collected. Each game has 12 rows: two sets of 5 rows for each of the team players and an additional row for each team’s summary statistics. Many stats are missing for the player rows and not missing for the team rows, and vice versa. This makes the missingness of the rows dependent on the type of columns (and therefore many of the other columns). However, this missingness is not missing by design because we cannot always infer one column’s missingness exactly from another in the columns that we had. 

Furthermore, special individual statistics were recorded differently based on the league the game took place in. It appeared that some leagues did not record the individual kill statistics in rows for the players and not the teams. <code class="language-plaintext highlighter-rouge">“killsat15”</code>, one of the individual kill statistics, we speculate will have its missingness dependent on the <code class="language-plaintext highlighter-rouge">“league”</code> column based on this fact.

| league     |      False |       True |
|:-----------|-----------:|-----------:|
| AL         | 0.0189112  | 0          |
| CBLOL      | 0.0264539  | 0          |
| CBLOLA     | 0.0271098  | 0          |
| CDF        | 0.00743332 | 0          |
| CT         | 0.00470048 | 0          |
| DDH        | 0.00940096 | 0          |
| EBL        | 0.0173808  | 0          |
| EL         | 0.00448185 | 0          |
| EM         | 0.029624   | 0          |
| EPL        | 0.00940096 | 0          |
| ESLOL      | 0.0330127  | 0          |
| GL         | 0.0097289  | 0          |
| GLL        | 0.0179274  | 0          |
| HC         | 0.0154132  | 0          |
| HM         | 0.0177088  | 0          |
| IC         | 0.00732401 | 0          |
| LAS        | 0.027547   | 0          |
| LCK        | 0.0532357  | 0          |
| LCKC       | 0.0552033  | 0          |
| LCO        | 0.0153039  | 0          |
| LCS        | 0.0288588  | 0          |
| LDL        | 0          | 0.527094   |
| LEC        | 0.031373   | 0          |
...
| UL         | 0.0267818  | 0          |
| VCS        | 0.0353083  | 0          |
| VL         | 0.00961959 | 0          |
| WLDs       | 0.0132269  | 0.00800493 |

<iframe src="assets/league_distribution_mar.html" width="800" height="600" frameBorder="0"></iframe>

<iframe src="assets/tvd_mar.html" width="800" height="600" frameBorder="0"></iframe>

| side   |   False |   True |
|:-------|--------:|-------:|
| Blue   |     0.5 |    0.5 |
| Red    |     0.5 |    0.5 |

<iframe src="assets/side_distribution_mcar.html" width="800" height="600" frameBorder="0"></iframe>

<iframe src="assets/tvd_mcar.html" width="800" height="600" frameBorder="0"></iframe>


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
