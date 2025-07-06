#Defining a custom funvtion

'''function that can find minimum between 3 numbers'''
from decimal import Decimal
(value1 := Decimal(input('Enter 3 numbers'))), (value2 := Decimal(input())), (value3 := Decimal(input()))
def minimum(value1,value2,value3):
    min_val = value1
    if value2 < min_val:
        min_val = value2
    if value3 < min_val:
        min_val = value3
    return min_val

print(minimum(value1,value2,value3))       