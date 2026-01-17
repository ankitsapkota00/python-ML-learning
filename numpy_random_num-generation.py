'''
Use numpy random number generation to create an array of twelve
random grades in the range 60 through 100, then reshape the result
into a 3 by 4 array. Calculate the avetage of all the grades,the averages
of grades in each column and of grades in each row
'''

import numpy as np

grades = np.random.randint(60, 101 , 12).reshape(3,4)

print(grades)

print("Average of all elameants: ",grades.mean())

print("Average of each column: ",grades.mean(axis = 0))

print("Average of each row: ", grades.mean(axis = 1))