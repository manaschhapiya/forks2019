str1 = input("enter the name of file")
with open(str1) as fp1:
        rad = fp1.readlines()
        print(rad[-1])


