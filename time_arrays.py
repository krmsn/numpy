import time
import numpy as np
import random

start_time_list = time.time()

array1 = np.random.randint(1, 7, 10_000_000)
print("Process finished --- %s seconds ---" % time.time() - start_time_list)
