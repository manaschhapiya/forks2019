with open('romeo.txt') as fp1:
    dict1 = {}
    for item in fp1.readlines():
        list1 = item.split(" ")
        for word in list1:
            if word not in dict1:
                dict1[word]=1
            else:
                dict1[word]=dict1[word]+1
                
   
        
            
            
    
