import numpy as np
'given list of integers print how many are even'

integers = [12, 45, 89, 38, 47, 90]
x = len(integers)
even = 0
for i in range(0,x):
    if integers[i] % 2 == 0:
        even += 1

print(f"{even} numbers are even")        
'''---------------------------------------------'''

'''Print all numbers form 1 to 50 divisible by 3 or 5'''
one_to_fifty = np.arange(1,51)

for i in range(50):
    if one_to_fifty[i] % 3 == 0:
        print(one_to_fifty[i], end=" ")
    elif one_to_fifty[i] % 5 == 0:
        print(one_to_fifty[i], end=" ")

'''---------------------------------------------------'''

'''------Given a string count the number of vowels-----'''
string = "Artificial intelligence"
count = 0
for i in string:
    if i in "aeiouAEIOU": #??
        count += 1

print("\nnumber of vowels are: ",count)

'''''reverse string without using slicing'''

length = len(string)
for j in range(length-1,-1,-1):
    print(string[j], end="")

#-------------------------------------------

'''Find the largest number in the list without using max()'''
greatest = integers[0]

for i in range(1,x):
    if integers[i] > greatest:
        greatest = integers[i]

print("\n Max value in list is:",greatest)

'''--------------------------------------------------------'''
'''Remove duplicates from a list and keep the same order'''
dup_list = [1, 2, 3, 3, 2, 5, 7, 6,6,6,8]

'''for i in range(1,len(dup_list)-1): the range(1,len(dup_list)-1) got calculated once
    for j in range(i-1,-1,-1):
        if dup_list[j] == dup_list[i]:
            dup_list.pop(i)           so when pop removed value and shrinked index it became out of range 

print("\n",dup_list) '''       

result =[]
for x in dup_list:
    if x not in result:
        result.append(x)

print(result)        
        