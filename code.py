pip install beautifulsoup4

pip install requests

#Import all the required modules, use "pip install module_name" to install modules

import sys
import time
from bs4 import BeautifulSoup
import requests

# The page may or may not grant access, so we need to use try and except block to handle that
try:
    page=requests.get("https://www.cricbuzz.com/")
except Exception as e:
    error_type,error_obj,error_info=sys.exc_info()
    print("ERROR FOR LINK:",url)
    print(error_type,"Line:",error_info.tb_lineno)
    
# Our scraper sends continues requests to the page, so to restrict that we need to make our
time.sleep(2)

# Our text will be consists of all the HTML code
soup=BeautifulSoup(page.text,"html.parser")

# Extract only required data by adding tag and attributes
links=soup.find_all('div',attrs={'class':"cb-nws-intr"})

# To check if request granted to scraper
page

#This gives all the HTML code from the pastsed link
soup

# Producing summary in a line by line format
k=1
for i in links:
    print(k,".",i.text)
    print("\n")
    k+=1
