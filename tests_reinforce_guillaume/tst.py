import random
import numpy as np

a = np.array([1,2,3])
b = np.array(["a","b","c"])

c = (1/a.sum())*a
print(random.choices(range(len(a)),weights=a))