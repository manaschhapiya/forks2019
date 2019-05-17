with open ('passwd') as fp1:
    dict1 = {}
    for line in fp1.readlines():
        list1 = line.split(":")
        if list1[0]=='#':
            continue
        else:
            dict1[list1[0]]=[list1[2]]
            
    print(dict1)
    
    list1 = list(sorted(dict1))
    
    
    for word in list1:
        print(word,"   ",dict1[word])
   
        
        
