def counter(item):
    list1 = ['13','14','17','18','19']
    a = len(item)
    sum=0;
    for i in range(0,a):
        if item[i] not in list1:
            sum = sum + int(item[i])
        else:
            pass
        
            
    return sum 

keys = input("enter the keys").split(" ")

value = input("enter the name").split(" ")

a = len(keys)

dict1 = dict({})


for i in range(0,a):
    dict1 [keys[i]] = value[i]
    
print(dict1)
    
list2   =list( dict1.values() ) 

 

print(counter(list2))   
 
       
            