'''to find the minimum and maximum in a list'''
n1 = int(input('enter a integer '))
n2 = int(input('enter another integer'))
n3 = int(input('enter another integer'))

minimum = n1
maximum = n1
 
if maximum < n2:
    maximum = n2

if  n2 < minimum:
    minimum = n2
    
if maximum < n3:
    maximum = n3

if  n3 < minimum:
    minimum = n3
    
print('minimum is',minimum     ,     'maximum is', maximum )
