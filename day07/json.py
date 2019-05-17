# -*- coding: utf-8 -*-
"""
Created on Tue May 14 11:09:33 2019

@author: Manas
"""
import requests

url1 = "http://api.openweathermap.org/data/2.5/weather"
url2 = "?q=Alwar"
url3 = "&appid=604f773b066ab45af94403eab941548b"

url = url1 + url2 + url3
print (url)


response = requests.get(url)

response.content




jsondata = response.json()



print (jsondata)


print('longitude',jsondata['coord']['lon'])
print("latitude",jsondata['coord']['lat'])
print("weather condition",jsondata['weather'][0]['description'])
print("wind speed",jsondata['wind']['speed'])
print("sun rise",jsondata['sys']['sunrise'])
print("sunset",jsondata['sys']['sunset'])

