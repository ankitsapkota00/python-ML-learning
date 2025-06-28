x = int(input('how many student\'s grade are you going to enter'))
x = x
total = 0
for y in range(x):
    z = int(input('enter a grade'))
    total += z
avg = total / (x)  
print ('Average of grades is',avg) 