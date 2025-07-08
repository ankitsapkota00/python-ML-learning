# Rolling a die 6,000,000 times

import random

frequency1 = 0
frequency2 = 0
frequency3 = 0
frequency4 = 0
frequency5 = 0
frequency6 = 0

for i in range(6_000_000):
    a = random.randrange(1,7)
    if a == 1:
      frequency1 += 1
    elif a == 2:
      frequency2 += 1
    elif a == 3:
      frequency3 += 1  
    elif a == 4:
      frequency4 += 1
    elif a == 5:
      frequency5 += 1
    elif a == 6:
      frequency6 += 1

print(f'Face {'Frequency' : >17}')
print(f'1 {frequency1 : >17} ')
print(f'2 {frequency2 : >17} ')
print(f'3 {frequency3 : >17} ')
print(f'4 {frequency4 : >17} ')
print(f'5 {frequency5 : >17} ')
print(f'6 {frequency6 : >17} ')

        

