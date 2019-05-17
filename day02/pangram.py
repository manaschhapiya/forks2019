str1 = "The quick brown fox jumps over the lazy dog"
count=0

str2 = "abcdefghijklmnopqrstuvwxyz"

for i in range(0,26):
    if str2[i] in str1:
        count=count+1
        pass
    
    else:
        print("not pangram")
        break
    if count==26:
        print("its pangram")
    