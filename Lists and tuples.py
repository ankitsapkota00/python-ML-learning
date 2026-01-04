fruits = ["apple","banana","cherry"]
print(fruits)

#accessing via index
print('first fruit', fruits[0])
print('last fruit', fruits[-1])

#modify elements
fruits[1] = 'blueberry'
print(fruits)

#adding elements/items to a list
fruits.append("mango")
print('after appending',fruits)

fruits.insert(1,'strawberry')
print('after inserting',fruits)

#remove elements
fruits.remove("cherry")
print('after removing',fruits)

popped = fruits.pop(2)
print('After popping', fruits)
print('popped items', popped)

#adding a bunch of fruits
fruits.append('kiwis')
fruits.append('pineapple')
fruits.append('guava')

print(fruits)
#slice elements
print('Every two fruits', fruits[::4])
print('Second to fourth fruits', fruits[1:4])
print('first three fruits', fruits[:3])
print('last two fruits', fruits[-2:])

#modify lists with slices
fruits[1:3] = ['grape', 'watermelon','cranberry']
print('after sliced modification', fruits)

#deleting slices
del fruits[-1]
print("After deleting sliced: ", fruits)



#creating tuples
coordinates = (10.5, 20.7, 30.2)
print('tuple', coordinates)

#
print('first coordintate',coordinates[0])

print('Slice a tuple', coordinates[-2])

#unpacking tuples
x, y, z = coordinates

print(f"X: {x}, Y: {y}, Z: {z}")