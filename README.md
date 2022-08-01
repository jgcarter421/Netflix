### Netflix Analysis

## Purpose
Our final project is in the style of "Shark Tank" where we will be trying to entice our instructors to fund the next best Netflix movie. We chose our data from [Kaggle](https://www.kaggle.com/datasets/victorsoeiro/netflix-tv-shows-and-movies?select=titles.csv).

### What makes a movie the best? 
We will be cleaning and sorting our data to find the "best" based upon IMDB scores and votes. Our goal is to weigh the IMDB score with the amount of votes to find the highest scores for movie rating, genre, runtime, actor, and director. We are omitting any films made outside the US and are limiting the type of media to movies only. Once we have determined what the "best" of each category is, we will be creating a flask app to make a website as advertisement for our mock movie! A machine learning model will be created to assist in predicting what our IMDB score might be. 

## Our project so far: 
We began cleaning our data using Google Collab with the pandas library. After converting our raw data into initial dataframes, we determined which columns had data we deemed impertinent to our analysis and dropped them. We dropped the columns for movie "description" and actor's "character" since we are not looking for best descriptions or characters based on IMDB scores. We also dropped the "seasons" column since seasons applies to TV shows- not on movies. We then filtered out all TV shows and all movies produced outside the United States.

We then used the ETL method to create two SQL databases. One of our databases has the movie data and the other has the actor/director data.   
Originally, we were going to merge our two databases, but we found that it duplicated our movie data since there were multiple actors credited for each movie.   
For example: without the merge we would have one set of data for the movie Titanic. If we merged the dataframes, we would then have several sets of duplicate data for each actor.  
Therefore, we kept the data separated and downloaded each dataframe into a new csv file: cleaned_credits.csv and cleaned_movie_db.csv.  

In conjunction with our SQL databases, we also created an entity relationship diagram.  
[![ERD](https://user-images.githubusercontent.com/96644316/182062124-d52cfd66-72bd-4460-b7f1-7488ead23090.png)]  
This diagram shows the major categories of data and how it will be broken down for further analysis in our quest to find the "best".

### What is next?
Next, we are training a machine learning model to predict what the IMDB score of what our mock movie will be. We are currently working on a neural network model in the "ml_prediction" branch of this repository. We will also be determining what qualifies as the "best" for each category by weighing the IMDB scores and votes.

### Limitations of analysis
The biggest limitation of our analysis is that an IMDB score is completely subjective. Any user registered to the website can submit a movie rating to contribute to the overall score.
Another limitation is the fact that our movie data extends from release dates as early as 1954 to present day. Present day movies are more likely to have a higher number of votes. It is also difficult to account for extenuating factors such as overall cultural impact and societal changes since older movies have released.
