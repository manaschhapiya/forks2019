"""

Code Challenge
  Name: 
    Regular Expression 2
  Filename: 
    
      
  Problem Statement:
    You are given N email addresses. 
    Your task is to print a list containing only valid email addresses in alphabetical order.
    Valid email addresses must follow these rules:

    It must have the username@websitename.extension format type.
    The username can only contain letters, digits, dashes and underscores.
    The website name can only have letters and digits.
    The minimum length is 2 and maximum length of the extension is 4. 
  Hint: 
    Using Regular Expression 
  Input:
    lara@hackerrank.com
    brian-23@hackerrank.com
    britts_54@hackerrank.com
  Output:
    ['brian-23@hackerrank.com', 'britts_54@hackerrank.com', 'lara@hackerrank.com']

"""

import re
list1 = []
result1 = []
while True:
    str1 =  input("enter the email")
    list1.append(str1)
    
    
    if not  str1:
        break
    
for item in list1:
    
    
    if re.findall(r'[a-zA-Z0-9-_]*@[a-zA-Z0-9]*\.[a-z]{2,4}',item):
        
        result1.append(item)
    
    
print(result1)
    
    
        
