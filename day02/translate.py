def translate(item):
    str2 = "aeiouAEIOU"
    str3 = ''
    a = len(item)
    for i in range(0,a):
        if item[i] not in str2:
           str3 = str3 + item[i]+"o"+item[i]
        else:
            str3 = str3 + item[i]
    print(str3)
        
        
        
        
            
            


str1 = input("enter the string")
translate(str1)