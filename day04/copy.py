with open('romeo.txt', mode='rt') as file :
   fp1 = open ("new1.txt",mode='wt')
   file1 = file.read()
   for i in file1:
       fp1.write(i)
   
   
