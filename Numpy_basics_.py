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


'''---------------------NumPy Calculation Methods-------------------------------'''

grades = np.array([[87, 96, 70], [100, 87, 90],
                  [94, 77, 90], [100, 81, 82]])

print(grades)

print(grades.sum())
print(grades.min())
print(grades.max())
print(grades.mean())
print(grades.std())
print(grades.var())

#Calculations by row(axis 1) or columns(axis 0)

print("Average of each column is: \n",grades.mean(axis = 0))
print("Average of each row is: \n\n", grades.mean(axis = 1))


'''------------------- Universal functions --------------------'''
nums = np.array([1, 4, 9, 16, 25, 36])
print(np.sqrt(nums))

nums2 = np.arange(1,7) * 10
print(np.add(nums, nums2))

'''-----------------------------Indexing and Slicing-------------------------'''
#arr[index]   indexing
#arr[start:stop:step]   slicing, stop is exclusive

trip = np.arange(23,56)
print(trip)

print("\n\nfirst element", trip[0])
print("\nthirteenth element",trip[13])

print("\nfirst 10 elements", trip[0:10])
print("\nLast 10 elements:", trip[-1:-11:-1],"\n\n")

#-----------------indexing & slicing 2dimensional arrays-------------------
grade = np.array([[87, 96, 70], [100, 87, 90],
                 [94, 77, 90], [100, 81, 82]])

print(grade)

print(grade[0,1],"\n\n")   #indexing-- giving a row index and column index for a specific element

#---------selecting subset of two dimensional array rows----------

#To select a single row, specify only one index in square brackets
print(grade[0],"\n\n")

#To select multiple sequential rows, slice notation is used
print(grade[0:2],"\n\n")
print(grade[2:4],"\n\n")

#To select multiple non sequential rows, use a list of row indices
print(grade[[1,3]],"\n\n")

#-------------Selecting a Subset of Two Dimensional array's Columns----------------
#                 arr[:,:] main syntax so you can get anything in 2D array
#you can select subsers of columns by providing a tuple specifying the row(s)
#and columns to select.

print(grade[:,0],"\n\n")
print(grade[:, 1:3],"\n\n")

#or specific column using list of column indices
print(grade[:,[0,2]])

'''-------------------Views:Shallow Copies AND Deep Copies---------------------'''
numbers3 = np.array([1,2,3,4,5,6])

numbers4 = numbers3.view()
print(f'\n\n{numbers4}\n')

numbers3[2] = 94
print(numbers4)  #number4 index value 2 also changes even though we only changed index value of number3

#Slicing also creates views

numbers4 = numbers3[0:3]

print(f'\n{numbers4}\n')

numbers3[0] = 22

print(f'\n{numbers4}\n')

#Deep Copies, change in one doesnt affect other

grade1 = np.arange(1,6)

grade2 = grade1.copy()

print(grade1)
print(grade2,'\n')

grade1[0] = 80

print(grade1)
print(grade2)


#---------------Reshaping and Transposing-------------
#method reshape returns a view with new dimension
#method resize does not returns None; just changes the original

milage = np.array([[47, 56, 30],[60, 47, 50]])
print(f'\n{milage}\n')

gin = milage.reshape(1,6)
print(gin,'\n\n',milage,'\n') #gin's dimension changed but milage's didn't

milage.resize(1,6)
print('\n',milage)

#-----flatten vs ravel-------(multidimensional to single dimension)
#flatten --> deep copies 
goals = np.array([[87, 96, 70], [100, 87, 90]])
print(f'\n Goals:\n {goals}\n')

flattend = goals.flatten()
print(f'\nFlattened:\n{flattend}\n')

print(f'Goals once agian:\n{grades}\n')

flattend[0] = 300
print(f'Flattend after element change:\n{flattend}\n')
print(f'\nGoals after change in flattend:\n {goals}\n')

#ravel ---> view of original array/ 
#goals will remain 2 dim ravel will remain 1 dim but change in element in any one will change the other
raveled = goals.ravel()
print(f'Raveled:\n{raveled}\n')
print(f'Goals:\n{goals}\n')

raveled[0] = 555
print(f'Raveled after element change:\n{raveled}\n')
print(f'Goals after change in raveled:\n{goals}\n')


#------------------ Transposing Rows and Columns---------------
#Transpose ------> view of original & doesnot modify original
print(f'Transposed \n{goals.T}\n')

#Horizontal and Vertical Stacking
goals2 = np.array([[94, 77, 90], [100, 81, 82]])

print(f'Horizontally stacked:\n{np.hstack((goals,goals2))}\n')
print(f'\nVerticlally stacked:\n{np.vstack((goals,goals2))}')


