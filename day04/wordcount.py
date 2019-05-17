'''
Code Challenge
  Name: 
    Word count
  Filename: 
    wordcount.py
  Problem Statement:
    Unix systems contain many utility functions. 
    One of the most useful to me is wc, the "word count" program. 
    If you run wc against a text file, it'll count the characters, words, 
    and lines that the file contains.
     
    The challenge for this exercise is to write a version of wc in Python. 
    However, your version of wc will return four different types of information 
    about the files:
 
        Number of characters (including whitespace)
        Number of words (separated by whitespace)
        Number of lines
        Number of unique words
    
    The program should ask the user for the name of an input file, 
    and then produce output for that file. 
    
'''




with open ("romeo.txt") as fp1:
    count = 0
    count1 = 0
    a = 0
    b = 0
    
    
    for item in fp1.readlines():
        b = b + 1
        count1 =  count1 + len(item.split(" "))
        a = a + (len(set(item.split(" "))))
        for item1 in item:
            count = count + 1
        
    print(a)    
        
    print(count)
    
    print(b)
        
    print(count1)
        
     
    
    
        
    
    
    
    
        
    
    

