state =   [ 'Alabama', 'California', 'Oklahoma', 'Florida']

list1 = ['a','e','i','o','u','A','E','I','O','U']
output  = []
for item in state:
    new = ''
    for char  in item:
        if char not in list1:
            new = new  + char
            
    output.append(new) 
    
print(output)




  