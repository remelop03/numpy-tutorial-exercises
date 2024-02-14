import numpy as np

arr = np.arange(0, 9)
reshape_arr = np.reshape(arr, (3, 3))

print(np.diag(reshape_arr))
