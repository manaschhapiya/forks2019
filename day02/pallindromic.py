def check(string):
    if string==string[::-1]:
        print("true")
        
    else:
        print("false")
        
        
list1 = ['12','83','93','113','3']
for item in list1:
        check(item) 
        break
      