# IPL Data Analytics

## Scraping player names from link:

Given constraint specified that the team has to be formed by only drawing players from the eight teams going to participate in IPL 2019.

To obtain a csv file of players to be considered during further data analysis, we built a Web Crawler which crawls through the website (http://www.espncricinfo.com/ci/content/squad/index.html?object=1165643) given to us and then through each team's link to obtain the desired data.

*BeautifulSoup* Python library was used and a html parsing of the page source resulted in a final list of 190 eligible players to choose from.
	
## Data Analysis:
 
 Our approach was focused on selecting the best performing players over the years, by using statistical information from the dataset.
 
 A quick analysis of the given dataset indicated that, data from the years prior to 2014 had inconsistent player names. Further, we decided to take into consideration current form and general consistency, because of which the statistical score of a player's performance in 2019, was determined by giving higher weightage to the more recent performances. Thus, we considered only the past 4 seasons of IPL player data.
	
  We created a single dataset comprising of Runs, Strike Rate, Wickets, Economy, Ct_St(catches & stumpings) and Matches played from the past 4 years.
  All players not participating in the 2019 IPL season were removed by using the names scraped from the url provided.
  We generated our own features from the data to summarise the performance of the players in their respective categories, i.e. Batting, Bowling and Allround.
	The columns generated were:
		1. Batting Average: Given by the runs scored / total matches played
		2. Wickets per match: Total wickets taken / total matches played
	
  Player's were given value 'IND' if they were from India, 'OVS' otherwise.
	
To summarise each player's performance in each department, we decided on creating metrics/scores using the data.
  1. 	For creating the Batting score metric, we selected the Batting Average and Strike Rate. We combined the two values in a single column called 'Batting Score'.
		The formula used was:
				Batting Score = Batting Average + 0.01 * Strike Rate
		This was done because we wanted the Batting Average to have a higher value in determining the Batting Score than the Strike Rate.
	
  2. 	For creating the Bowling score metric, we selected the Wicket_per_match and Economy. We combined the two values in a single column called 'Bowling Score'.
		The formula used was:
				Batting Score = ( Bowling Average - 0.005 * Economy ) * Total matches played
		Here, the higher the Economy, the lesser is the value of the bowler's performance. Hence the Economy was given a negative weightage. We also multiplied the resulting value with the matches played, to nullify the effect of those player's who played only a few matches and performed well. This was done in order to account for general consistency of the player.
		
  3. The Allround score was calculated as the sum of the Bowling and Batting scores.
				Allround Score = Batting Score + Bowling Score
				

  Finally, we achieved scores for each player, in each department, for each year. In order to combine the scores from each year, we gave decreasing weightage over the years.
	
  - Total Batting Score = Batting Score 2018 + 0.8 * Batting Score 2017 + 0.6 * Batting Score 2016 + 0.4 * Batting Score 2015
	- Total Bowling Score = Bowling Score 2018 + 0.8 * Bowling Score 2017 + 0.6 * Bowling Score 2016 + 0.4 * Bowling Score 2015
	- Total Allround Score = Allround Score 2018 + 0.8 * Allround Score 2017 + 0.6 * Allround Score 2016 + 0.4 * Allround Score 2015
		
	This gave us 3 columns culminating the player's performance scores over the 4 years. Based on this data generated, we sorted values in each column and then selected the best players from each department.
	
## Final Result:

  1. The list of top 10 players of each category is stored in ipl_batsmen.csv , ipl_bowlers.csv and ipl_allrounders.csv files respectively.
  2. For Batsmen:
			Top 5 batsmen are selected which included 3 Indian players and 2 foreign players.
	3. For Bowlers:
			Top 3 bowlers are selected from ipl_bowlers.csv. Each of them are Indian.
	4. For Allrounders:
			Top 2 allrounders are selected from ipl_allrounders.csv file which includes one Indian player and  one foreign player.
		
  Thus, the team of 11 optimal players has been selected out of which 4 players are foreign.
	
  - Selection of the Wicketkeeper
    The batsman with the highest score of total catches/stumps is selected to be the wicket keeper. In this case, the wicket keeper is determined to be AB De Villiers.
	
	- Selection of Captain
  Virat Kohli, selected based on being the player with the highest score.
  
	- Selection of Vice Captain
   Kane Williamson, selected based on being the oversea player with highest score.
			
  Final selected 11 players and their respective positions are present in the final_11.csv files.
	

