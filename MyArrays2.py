import numpy as np

grades = np.array([[87, 96, 70], 
                   [100, 87, 90],
                   [94, 77, 90], 
                   [100, 81, 82]])


print("\n\n\n")


print("Sum score:", grades.sum())
print("Minimum score:", grades.min())
print("Maximum score:", grades.max())
print("Average score:", grades.mean())
print("Standard deviation of scores:", grades.std())
print("Variance of scores:", grades.var())


print("\n\n\n")


numbers = [1 ,4 ,9, 16, 25, 36]
print((np.sqrt(numbers)))


print("\n\n\n")


print(grades.mean(axis = 0))
print(grades.mean(axis = 1))


print("\n\n\n")


grades = np.array([[87, 96, 70], 
                   [100, 87, 90],
                   [94, 77, 90], 
                   [100, 81, 82]])

print(grades[0,1])
print(grades[1])
print(grades[1, 2])
print(grades[[1, 3]])
print(grades[:, 0])
print(grades[0, :])
print(grades[:, 1:3])       #   Just like MATLAB.


print("\n\n\n")


# Shallow copies

numbers = np.arange(1, 6)
number2 = numbers.view()

print(number2)

numbers[1] *= 10

print(number2)

number2[1] /= 10

print(number2)

numbers2 = numbers[0:3]

print(numbers2)


print("\n\n\n")


# Deep copies
numbers2 = numbers.copy()

grades = np.array([[87, 96, 70], [100, 87, 90]])
print(grades.reshape(1, 6))
print(grades)

flattened = grades.flatten()
print(flattened)
print(grades)

ravelled = grades.ravel()
print(ravelled)
print(grades)

ravelled[5] = 99
print(grades)

grades2 = np.array([[94, 77, 90], [100, 81, 82]])

h_grades = np.hstack((grades, grades2))
print(h_grades)

v_grades = np.vstack((grades, grades2))
print(v_grades)
