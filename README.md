# League of Legends Having More kills Than Lane Oponnent Winrate Analysis

by Ahmed Mostafa and Ethan Vo (ahmostafa@ucsd.edu, etvo@ucsd.edu)

---

## Introduction

Our dataset is on all of the professional League of Legends games that have taken place in 2023. The dataset contains 12 rows per game, one row per player and 2 rows of summary statistics (one for each team). Furthermore, there are over 100 columns of nearly all the data you could collect on a league of legends match. Our question is “Which player position, when achieving more kills than their lane opponent has the greatest impact on boosting the overall win rate?” Addressing this question would help managers choose the players for each team where the player who know how to kill the most should play in that specific position. Although the data does not explicitly collect information on whether a player has more kills than a lane opponent, we can collect the data from columns “kills”, “positions”, and “side”  to compare the kills of a player and their lane opponent and make our own column “has_more_kills.”

League of Legends players have always debated on which position needs kills to help the team win. As players continue to play League of Legends and try out the different positions on a team, players may get curious as to which position has the greatest influence on the game with more kills. Through this experiment they can know which position needs more kills than their lane opponent the most to help their team win.

The columns we are interested in to answer, “Which player position, when achieving more kills than their lane opponent has the greatest impact on boosting the overall win rate?” are: <code class="language-plaintext highlighter-rouge">“gameid”</code>, <code class="language-plaintext highlighter-rouge">“league”</code>, <code class="language-plaintext highlighter-rouge">“side”</code>, <code class="language-plaintext highlighter-rouge">“position”</code>, <code class="language-plaintext highlighter-rouge">“result”</code>, <code class="language-plaintext highlighter-rouge">“kills”</code>, and <code class="language-plaintext highlighter-rouge">“killsat15”</code>. These are the columns from the dataset that are relevant to our proposed question, as they provide us with information about the position, the side they belong to, whether the position won or lost, and the number of kills done by each position. In the process of cleaning, we removed rows that belong to the team, as they were irrelevant to our analysis, and sorted the data to have each position next to its opponent for easier visual comparison. After that, we decided to add the boolean column, <code class="language-plaintext highlighter-rouge">“has_more_kills”</code>, where True means the position had more kills, and False otherwise. The column was added to simplify the analysis and comparison process. After cleaning, our dataframe had 107720 rows, representing 10772 games, and 8 columns.

Descriptions of Columns

* <code class="language-plaintext highlighter-rouge">"gameid"</code> is the identification number of the particular game from that tournament. This is unique for all games in the dataset
* <code class="language-plaintext highlighter-rouge">“league”</code> is the professional league that the game is taking place in
* <code class="language-plaintext highlighter-rouge">"side"</code> is the side that player played on. This can either be red or blue (corresponding to the red and blue sides on the map for League of Legends)
* <code class="language-plaintext highlighter-rouge">“position”</code> is the position or role the player played. This can be “top”, “mid”, “bot”, “jng”, or “sup” for the five positions in League of Legends
* <code class="language-plaintext highlighter-rouge">“result”</code> is whether or not the team won. It will be 1 if the player’s team won or 0 for a loss
* <code class="language-plaintext highlighter-rouge">"kills"</code> is the number of kills that particular player got in that game
* <code class="language-plaintext highlighter-rouge">“killsat15”</code> is the number of kills a player got within the first 15 minutes of the particular game
* <code class="language-plaintext highlighter-rouge">“has_more_kills”</code> states whether or not the player has more kills than their lane opponent. It is a boolean that returns either “True” or “False”

---

## Data Cleaning and Exploratory Data Analysis

We first decided to only keep the columns relevant to our question: <code class="language-plaintext highlighter-rouge">“gameid”</code>, <code class="language-plaintext highlighter-rouge">“league”</code>, <code class="language-plaintext highlighter-rouge">“side”</code>, <code class="language-plaintext highlighter-rouge">“position”</code>, <code class="language-plaintext highlighter-rouge">“result”</code>, <code class="language-plaintext highlighter-rouge">“kills”</code>, <code class="language-plaintext highlighter-rouge">“killsat15”</code>, and <code class="language-plaintext highlighter-rouge">“has_more_kills”</code>. We cleaned the data by removing the rows that contain information about the team, as we are comparing data at the scope of the players, not the teams. We did this by removing the rows that had "team" as its entry in the <code class="language-plaintext highlighter-rouge">“position”</code> column. We then added a new column to the DataFrame that identifying whether each row belongs to a position that had more kills than its counterpart in the opposing team. In order to create this column, <code class="language-plaintext highlighter-rouge">“has_more_kills”</code>, we took the rows with the same <code class="language-plaintext highlighter-rouge">“gameid”</code> and <code class="language-plaintext highlighter-rouge">“position”</code>, and compared the kills between the two sides. Our result is showed below:

| gameid             | league   | side   | position   |   result |   kills |   killsat15 | has_more_kills   |
|:-------------------|:---------|:-------|:-----------|---------:|--------:|------------:|:-----------------|
| 10000-10000_game_1 | LDL      | Red    | bot        |        1 |      11 |         nan | True             |
| 10000-10000_game_1 | LDL      | Blue   | bot        |        0 |       3 |         nan | False            |
| 10000-10000_game_1 | LDL      | Red    | jng        |        1 |       7 |         nan | True             |
| 10000-10000_game_1 | LDL      | Blue   | jng        |        0 |       0 |         nan | False            |
| 10000-10000_game_1 | LDL      | Red    | mid        |        1 |       2 |         nan | True             |

Univariate Charts

In order to increase our awareness of the data, we produced an interactive pie chart using <code class="language-plaintext highlighter-rouge">“plotly”</code> that reprensents the percentage of players who had more kills and won vs players who had more kills but lost. This visualization is helpful to give us insight of what to expect from our proportions that represent the impact of having more kills. We can see that 79.4% of the players who had more kills won. This finding made us expect that having more kills should impact on chances of victory.

<iframe src="assets/piechart.html" width="800" height="600" frameBorder="0"></iframe>


Then, we decided to see the distribution of kills per position for players won vs lost. The distribution would allow us to compare the kills distribution for winning vs losing players in the same position. This furthers our understanding and awareness of the data and back our expectations with reason. 
The histogram below shows the distribution of kills counts per position for winning vs losing players:

<iframe src="assets/histogram_distribution.html" width="800" height="600" frameBorder="0"></iframe>

As shown in the histogram, winning players generally had more kills than losing players. There is an anomaly where it appears that support(<code class="language-plaintext highlighter-rouge">“sup”</code>) distributions are closer to 0 than they are to the other positions. This could be explained by support positions normally defering kills to their teammates and focussing on supporting them rather than killing.

---
Bivariate Chart

After expanding our knowledge and understanding of the data, we started our analysis by plotting the following bar graph, which shows the win rate when the player has more kills than their lane opponent. 

<iframe src="assets/more_kills_barchart.html" width="800" height="600" frameBorder="0"></iframe>

As we anticipated, the support position has a relatively lower win rate when the player has more kills compared to their counterpart on the opposite team.

After that, we got our test statistic by plotting the following bar graph, which shows the difference in win rate when having more kills than their lane opponent, versus having less kills. 

<iframe src="assets/increase_win_rate_barchart.html" width="800" height="600" frameBorder="0"></iframe>

One intriguing observation is that the support role actually has a negative difference in win rate, which means that when support has more kills, it is less likely that the team wins. This motivated us to further invesitgate and verify our observation in our hypothesis testing.

Interesting Aggregates

While we were in the analysis process, we decided to look over an interesting aggregate, which is the mean kills per position when the position won and when the position lost. To calculate the means, we made a pivot table where the positions are the columns and the winning statuses are the rows.

|   result |     bot |     jng |     mid |     sup |     top |
|---------:|--------:|--------:|--------:|--------:|--------:|
|        0 | 2.72391 | 1.80124 | 2.27191 | 0.58225 | 1.70358 |
|        1 | 6.27757 | 3.46807 | 4.85156 | 1.01652 | 3.5129  |

Across all roles, the players that win on average have a higher number of kills than if they lose.

---

## Assessment of Missingness

NMAR Analysis

We believe that many columns in our data are not missing at random (NMAR) due to the way this data is recorded. Each game has 12 rows: two sets of 5 rows for each of the team players and an additional row for each team’s summary statistics. Many statistics are missing for the player rows and not missing for the team rows, and vice versa. This makes the missingness of the rows dependent on the type of columns (and therefore many of the other columns). However, this missingness is not missing by design because we cannot always infer one column’s missingness exactly from another in the columns that we have.

Furthermore, special individual statistics were recorded differently based on the league the game took place in. It appeared that some leagues did not record the individual kill statistics in rows for the players, only for the teams. <code class="language-plaintext highlighter-rouge">“killsat15”</code>, one of the individual kill statistics, we speculate will have its missingness dependent on the <code class="language-plaintext highlighter-rouge">“league”</code> column based on this fact.

Missingness Dependency

Looking through the data, we were interesting in assessing the missingness of <code class="language-plaintext highlighter-rouge">“killsat15”</code>  and verifying whether it depends on the <code class="language-plaintext highlighter-rouge">“league”</code> or not. This would help us identify whether <code class="language-plaintext highlighter-rouge">“killsat15”</code> is missing at random (MAR) or missing completely at random (MCAR).

We started by getting and plotting the distribution of missingness of <code class="language-plaintext highlighter-rouge">“killsat15”</code> for each <code class="language-plaintext highlighter-rouge">“league”</code>, where False means that it is missing, and True means it is present:

<iframe src="assets/league_distribution_mar.html" width="800" height="600" frameBorder="0"></iframe>

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
| LFL        | 0.0264539  | 0          |
| LFL2       | 0.0272191  | 0          |
| LHE        | 0.0064495  | 0          |
| LJL        | 0.0282029  | 0          |
| LJLA       | 0.0100568  | 0          |
| LLA        | 0.0209882  | 0          |
| LMF        | 0.00940096 | 0          |
| LPL        | 0          | 0.464901   |
| LPLOL      | 0.0174902  | 0          |
| LRN        | 0.0126804  | 0          |
| LRS        | 0.0130083  | 0          |
| LVP SL     | 0.0268911  | 0          |
| MSI        | 0.00830783 | 0          |
| NACL       | 0.0947748  | 0          |
| NEXO       | 0.018474   | 0          |
| NLC        | 0.0171622  | 0          |
| PCS        | 0.0320289  | 0          |
| PGN        | 0.021972   | 0          |
| PRM        | 0.0264539  | 0          |
| SL (LATAM) | 0.00983822 | 0          |
| TCL        | 0.0196764  | 0          |
| UL         | 0.0267818  | 0          |
| VCS        | 0.0353083  | 0          |
| VL         | 0.00961959 | 0          |
| WLDs       | 0.0132269  | 0.00800493 |

As we can see from the plot, two leagues <code class="language-plaintext highlighter-rouge">“LPL”</code> and <code class="language-plaintext highlighter-rouge">“LDL”</code> clearly have more True values, which means <code class="language-plaintext highlighter-rouge">“killsat15”</code> is missing for those two leagues significantly more than the other leagues.

We continued with our test and ran a permutation test with total variation distance (TVD) as the test statistic and a significance level of 5%.

Our observed total variation distance (TVD) was: .992

After running the permutation test, we got a p-value of 0.0, so we concluded that the missingness of <code class="language-plaintext highlighter-rouge">“killsat15”</code> is dependent on the <code class="language-plaintext highlighter-rouge">“league”</code> column, making the missingness type for <code class="language-plaintext highlighter-rouge">“killsat15”</code> missing at random (MAR) with dependency on <code class="language-plaintext highlighter-rouge">“league”</code>.

Here is the empirical distribution of the TVDs:

<iframe src="assets/tvd_mar.html" width="800" height="600" frameBorder="0"></iframe>

We also wanted to determine whether <code class="language-plaintext highlighter-rouge">“killsat15”</code> missingness depend on <code class="language-plaintext highlighter-rouge">“side”</code> or not.

Here is the distribution of the missingness of <code class="language-plaintext highlighter-rouge">“killsat15”</code>:

| side   |   False |   True |
|:-------|--------:|-------:|
| Blue   |     0.5 |    0.5 |
| Red    |     0.5 |    0.5 |

<iframe src="assets/side_distribution_mcar.html" width="800" height="600" frameBorder="0"></iframe>

This shows the distribution of missingness for <code class="language-plaintext highlighter-rouge">“killsat15”</code> and their respective means. The missingness of <code class="language-plaintext highlighter-rouge">“killsat15”</code> is perfectly split between the two sides, <code class="language-plaintext highlighter-rouge">“Blue”</code> and <code class="language-plaintext highlighter-rouge">“Red”</code>.

Our observed total variation distance (TVD) was: 0.0

Our p-value was: 1.0

This drove us to the conclusion that the missingness of <code class="language-plaintext highlighter-rouge">“killsat15”</code> does not depend on the <code class="language-plaintext highlighter-rouge">“side”</code> column.

Here is the empirical distribution of the TVDs:

<iframe src="assets/tvd_mcar.html" width="800" height="600" frameBorder="0"></iframe>

---

## Hypothesis Testing

The data used in our hypothesis testing did not have any rows without values. <code class="language-plaintext highlighter-rouge">“kills”</code> were recorded in every single game for each player in the dataset, so we did not need to impute or drop any data in order to complete the data for our hypothesis testing.

**Null Hypothesis**: The proportion of support position winning and having higher kills is equal to the proportion of support position winning and having less kills.<br>
**Alternative Hypothesis**: The proportion of support position winning and having higher kills is less than the proportion of support position winning and having less kills.

Our null and alternative hypotheses were driven from our observation of the change in win rate for the support position based on whether they had more kills or not. Our test Statistic will be the difference between the proportion of games won while having more kills and the proportion of the games won while having less kills. We will be testing on a significance level of 5%. The cutoff was chosen because it is the most used in the analysis field.

Result:
After running 100,000 simulations and checking probability of the observation in the data occurance, we got a p-value of 0.

#### Conclusion: 
Our test was statistically significant, so we reject the null hypothesis. The observation we saw in our data did not happen due to random chance, so we conclude that support having more kills may be detrimental to the team winning the game.


---
