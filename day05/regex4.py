"""

Code Challenge
  Name: 
    Regular Expression 4
  Filename: 
    regex4.py
  Problem Statement:
    You are given email addresses. 
    Your task is to print a list containing only valid email addresses in lexicographical order .
    (Take input from User)

    Valid email addresses must follow these rules:

    It must have the username@websitename.extension format type.
    The username can only contain letters, digits, dashes and underscores. 
    The website name can only have letters and digits. 
    The maximum length of the extension is  
 
  Hint: 
    Using Regular Expression 
  Input:
    ajeet@forsk.com
    kunal-23@forsk.com
    yogendra_54@forsk.com
  Output:
    ['ajeet@forsk.com', 'kunal-23@forsk.com', 'yogendra_54@forsk.com’]

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
    
    
result2= sorted(result1)

for item in result2:
    print(item)