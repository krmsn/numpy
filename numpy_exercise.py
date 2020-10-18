import numpy as np
import random 

grade_list = np.random.randint(60, 101, 12).reshape(3, 4)

print(grade_list)

print("All grades:", grade_list.mean())

print("Average by each test:", grade_list.mean(axis = 0))

print("Average by each student:", grade_list.mean(axis = 1))
