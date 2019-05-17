num = 0

while num<=100:
    if num%3==0 and num%5==0:
        print("fizzbuzz")
        num=num+1
        
    if num%3==0:
        print ("fizz")
        num=num+1
        
    if num%5==0:
        print("buzz")
        num=num+1
        
    
    else:
        print (num)
        num = num+1
        



