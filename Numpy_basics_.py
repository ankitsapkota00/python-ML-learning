import numpy as np

integers = np.array([[1, 2, 3], [4, 5, 6], [7,8,9], [13,4,2]])
print(integers)

floats = np.array([0.0, 3.55, 44.6,23.2])
print(floats)

print()
print()

print (integers.dtype)
print(floats.dtype)

#----------------------Arrays' dimension ----------------------------
print(integers.ndim) #dimension/axes/ think of a grid 
print(floats.ndim)

print(integers.shape) #returns tuple of rows and columns
print(floats.shape)

print(integers.size) #returns total number of elements

print(floats.itemsize) #returns total number of bytes required to store each element
print()
#------------------------------------------------------------------


# -----------------   Iteration in numpy arrays   ------------------

# for 1D arrays it will go element by element   ----------
for x in floats:
    print(x)

print()
print()



#for 2D arrays it will take the whole row    -----------
for y in integers:
    print(y)

print()
print()
#Iterating through the each element in 2D arrays -------

for x in integers:
    for y in x:
        print(y)
print()

#         Can iterate multidimensional arrays as if were one dimensional
#          using flat attribute

for i in integers.flat:
    print(i, end=' ')
    
#-----------------------------------------------------------------------------


'''--------------------Filling Arrays with specific value----------------------'''
#filling with zeros np.zero
#filling with ones np.one
#filling with any specific value np.full((dimension(inside braces), specific value)

print(np.zeros(7))  #one argument so one dimension array
print(np.ones((4,5)))  #tuple as argument so two dimensional array
print(np.full((4,5), 7)) 

print()
print()

'''-------------------------Creating arrays form ranges--------------------------'''
#np.arange ,just like built in python range but more optimized, 

print(np.arange(3))
print(np.arange(3,9))
print(np.arange(1,120,30))
print(np.arange(5,1,-1))
print()

#Creating evenly spaced Floating-Point Ranges with linspace (arithmetic progression)
#np.linspace(start, end, totalnumbers(including start and end))

print(np.linspace(0.0 , 15.0, 25))
print()
print()

#Reshaping an array   ---- using .reshape( , ) method
print(np.arange(1,31).reshape(6,5))
print()

'''--------------------------- Array Operators -----------------------------'''

#Arithmetic operations with arrays and Individual Numeric Values
numbers = np.arange(1,10)
print(numbers)

print(numbers * 2)  #each number will get multiplied by 2
print(numbers, "\n\n")

#Arithmetic operations between arrays---need to be same shape and operation
#happens between same index value element

numbers2 = np.linspace(1.1, 5.5, 9)
print(numbers2)

print(numbers * numbers2,"\n\n")

print(numbers - numbers2)


#Comparing Arrays
#------- with a value -------
a = np.arange(1,5)
print(a > 2,"\n")

#------- two arrays --------
b = np.array([1, 3, 2, 4])
print(a == b, "\n")

#------- boolean indexing ------
#if its true --> take the element at that position
#Boolean indexing = condition --> True/False array --> takes true value elements
print(a[a < 3],"\n")

mask = b != 4
print(b[mask])



