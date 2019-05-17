str1 = input("enter the string")

str2 = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

str3 = '1234567890'

alpha = 0

digit = 0


for i in str1:
    if i in str2:
        alpha = alpha + 1
        
for j in str1:
    if j in str3:
        digit = digit  + 1
        
        
print(alpha)
print(digit)