day = ['Monday','Tuesday']

list1 = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
 
for item in list1:
    if item not in day:
        day.append(item)
        
day1 = tuple(day)

print(day1)

