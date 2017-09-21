import numpy as np
i = np.random.random(15)
print(i)
print("Maximum numbber of array is", max(i))
i[i.argmax()]=100
print("Maximum number of array is", max(i))