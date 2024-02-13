import numpy as np

arr = np.ones((3, 3))

arr_padded = np.pad(arr, pad_width=1)


print(arr_padded)
