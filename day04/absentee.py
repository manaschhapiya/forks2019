with open('wor.txt', mode='wt') as file :
    count = 0
    for item in range(0,25):
        if count<25:
            str1 = input("enter the name")
            file.write(str1+"\n")
            count = count+1
            if str1=="":
                break
            
        else:
            print("limit reached")
            break
fp1 = open('wor.txt',mode='rt')
fp1.seek(0,0)
fp1.readlines()
                