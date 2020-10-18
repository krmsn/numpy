import numpy as np

integers = np.array([1, 2, 3])

print(integers)
print(type(integers))


print("\n\n\n")


integers = np.array([[1, 2, 3], [4, 5, 6]])

print(integers.dtype)       # 
print(integers.ndim)        # number of dimensions
print(integers.shape)       # shape of the array, in (number of rows, number of columns)
print(integers.size)        # number of elements in an array
print(integers.itemsize)    # 


print("\n\n\n")


for row in integers:
    print(row)

    for col in row:
        print(col, end = " ")
    print("\n")


print("\n\n\n")


for i in integers.flat:
    print(i, end = " ")


print("\n\n\n")


print(np.zeros(5))     # create an array of five zeroes.
print(np.ones(5))      # create a array of five ones.


print("\n\n\n")


array1 = np.ones((2, 4), dtype = int)
print(array1)


print("\n\n\n")


array2 = np.full((3,5), 13)
print(array2)


print("\n\n\n")


print(np.arange(5))
print(np.arange(5, 10))
print(np.arange(10, 1, -2))
print(np.linspace(0.0, 1.0, num = 5))


print("\n\n\n")


array1 = np.arange(1, 21)
print(array1)
array2 = array1.reshape(4, 5)
print(array2)


print("\n\n\n")


array3 = np.arange(1, 100001).reshape(4,25000)
print(array3)


print("\n\n\n")


array4 = np.arange(1,100001).reshape(100,1000)
print(array4)


print("\n\n\n")


numbers = np.arange(1, 6)
numbers *= 2          #   "Broadcasting"
print(numbers)


print("\n\n\n")


print(numbers >= 13)

numbers2 = np.arange(5, 10)

print(numbers > numbers2)
print(numbers == numbers2)


