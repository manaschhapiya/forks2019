str1 = input("enter the string 1")

str2 = input("enter the string 2")

a = len(str1)

b = len(str2)

count= 0

if a == b:
    for i in str1:
        if i in str2:
            count = count+ 1
            pass
        else:
            print("not anagram")
            
    if count == a:
        
        print("yes ! its anagram")
    else:
        print("nop")
    
else:
    print("not ")