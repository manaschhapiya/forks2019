"""
Code Challenge
  Name: 
    Currency Converter Convert  from USD to INR
  Filename: 
    currecncyconv.py
  Problem Statement:
    You need to fetch the current conversion prices from the JSON  
    using REST API
  Hint:
    http://free.currencyconverterapi.com/api/v5/convert?q=USD_INR&compact=y
    Check with http://api.fixer.io/latest?base=USD&symbol=EUR
    
"""


import requests
number = int(input("enter the amount"))



response = requests.get('https://free.currconv.com/api/v7/convert?q=USD_INR&compact=ultra&apiKey=300c0f526b16b1ed75fd')

response.content




jsondata = response.json()



print (number*jsondata['USD_INR'])