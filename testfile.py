
import numpy as np

n = np.ones(5)  # Original 1-dimensional array
n_2d = n[:, np.newaxis]  # Add a new dimension as the second axis (columns)
n_3d = n[np.newaxis, :, np.newaxis]  # Add new dimensions at the beginning and end

print(n.shape)  # Output: (5,)
print(n_2d.shape)  # Output: (5, 1)
print(n_3d.shape)  # Output: (1, 5, 1)