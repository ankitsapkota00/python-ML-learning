#take 4 integer input from a loop and find sum average min and max

total = 0
average = 0 
min = None
max = None
count = 0

for i in range(4):
    num = int(input('Enter a integer'))
    total += num
    count += 1

    if min is None or num < min:
       min = num

    if max is None or num > max:
       max = num

average = total/count  
print('The sum of these integers is ', total)
print('The average is ', average)
print('The minimum is ', min)
print('The maximum is ', max)