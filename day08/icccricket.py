"""
Code Challenge
  Name: 
    Webscrapping ICC Cricket Page
  Filename: 
    icccricket.py
  Problem Statement:
    Write a Python code to Scrap data from ICC Ranking's 
    page and get the ranking table for ODI's (Men). 
    Create a DataFrame using pandas to store the information.
  Hint: 
    https://www.icc-cricket.com/rankings/mens/team-rankings/odi 
    
    
    #https://www.icc-cricket.com/rankings/mens/team-rankings/t20i
    #https://www.icc-cricket.com/rankings/mens/team-rankings/test
"""


from bs4 import BeautifulSoup
import requests
import pandas as pd
from collections import OrderedDict

source = requests.get("https://www.icc-cricket.com/rankings/mens/team-rankings/odi").text

soup = BeautifulSoup(source,"lxml")

print (soup.prettify())



right_table=soup.find('table', class_="table")

print (right_table)

a = []
b = []
c = []
d = []

for item in right_table.findAll("tr"):
    online = item.findAll("td")
    
    if len(online)==5:
        a.append(online[1].text.strip())
        b.append(online[2].text.strip())
        c.append(online[3].text.strip())
        d.append(online[4].text.strip())
        
col_name = ["position","weighted matches","points","rating"]

col_data = OrderedDict(zip(col_name,[a,b,c,d]))
df = pd.DataFrame(col_data) 
df.to_csv("former.csv")


