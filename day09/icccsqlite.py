"""

Scrap the data from the URL below and store in sqlite database

https://www.icc-cricket.com/rankings/mens/team-rankings/odi


"""



from bs4 import BeautifulSoup
import requests
import sqlite3

conn = sqlite3.connect ( 'cricket.db' )
c = conn.cursor()


c.execute ("""CREATE TABLE batsman(
          
          position  TEXT,
          
          matches TEXT,
          points TEXT,
          rating TEXT
          
          )""")



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
        
        
for i in range(0,16):
    c.execute("INSERT INTO batsman VALUES ('TEXT(a[i])','TEXT(b[i])','TEXT(c[i])','TEXT(d[i]')")
    
    

c.execute("SELECT * FROM batsman")

print ( c.fetchall() )


conn.commit()

# STEP 7
# closing the connection 
conn.close()
        
        