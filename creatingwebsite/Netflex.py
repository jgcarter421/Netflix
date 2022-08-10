# Import Splinter and BeautifulSoup
import csv
from json import load
from matplotlib.pyplot import title
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager

#app = Flask(__name__)

# Dependencies and Setup

import pandas as pd

# Import csv
cleaned_credits_df = pd.read_csv("Resources/cleaned_credits.csv")
cleaned_movie_db_df= pd.read_csv("Resources/cleaned_movie_db.csv")
cleaned_credits_df.to_html("cleaneddata.html")
cleaned_movie_db_df.to_html("cleanedtitle.html")




