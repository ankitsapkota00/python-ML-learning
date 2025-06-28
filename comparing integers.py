#fig02_01.py
""" comparing integers using if statements and comparision operators"""

print('Enter two integers, and I will tell you',
      'the relation they satisfy.')

# read first integer
number1 = int(input('Enter an integer :'))

# read second integer
number2 = int(input('Enter another integer:'))

# Telling how to process

if number1 == number2:
    print(number1, 'is equal to', number2)

if number1 != number2:
    print(number1,'is not equal to',number2)

if number1 < number2:
    print(number1,'is less than',number2)

if number1 > number2:
    print(number1,'is greater than',number2)

if number1 <= number2:
    print(number1, 'is less than or equal to', number2)          
        
if number1 >= number2:
    print(number1,'is greater than or equal to', number2)

    


