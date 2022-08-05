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
credit_df = pd.read_csv("Resources/credits.csv")
title_df= pd.read_csv("Resources/titles.csv")
credit_df.to_html("credits.html")
title_df.to_html("title.html")






