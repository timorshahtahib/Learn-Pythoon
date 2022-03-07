# Python program to inverse
# a matrix using numpy

# Import required package
import numpy as np

# Taking a 3 * 3 matrix
A = np.array([[1, 2, 3],
			[0, 1, 4],
			[5, 6, 0]])




print("Matrix")
print(A)
print("\n")
print("Inverce Of Matrix")
# Calculating the invesre of the matrix
print(np.linalg.inv(A))
