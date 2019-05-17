def calculate(item):
    b = len(item)
    sum =0
    
    for i in range(0,b):
        if item[i]=='13':
            continue
        if item[i-1]=='13':
            continue
            
        
            
            
            
            
        else:
            sum = sum  +  int(item[i])
          
          
    return sum
    
    
    

str1 = input("enter the number").split(" ")

a = len(str1)

if a==0:
    print("sum is zero")
else:
    print(calculate(str1))
    