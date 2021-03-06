# R program to find inverse of a Matrix

# Create 3 different vectors
# using combine method.
a1 <- c(1, 5, 3)
a2 <- c(0, 3, 4)
a3 <- c(5, 3, 3)

# bind the three vectors into a matrix
# using rbind() which is basically
# row-wise binding.
A <- rbind(a1, a2, a3)

# print the original matrix
print("Matrix")
print(A)

# Use the solve() function
# to calculate the inverse.

print("Inverce Of Matrix")
T1 <- solve(A)

# print the inverse of the matrix.
print(T1)


print(T1%*%A)

