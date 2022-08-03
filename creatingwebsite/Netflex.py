# Import Splinter and BeautifulSoup
import csv
from json import load
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager

app = Flask(__name__)



# Dependencies and Setup
import pandas as pd
# Import csv
Netflex_to_load = ("Bootcampgithub", "cleaned_credits.csv")
Netflex_to_load = ("Bootcampgithub", "titles.csv")
Netflex_df = pd.read.csv("cleaned_credits.csv")
df = pd.read.csv


# Set up Splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)

html = browser.html
news_soup = soup(html, 'html.parser')




