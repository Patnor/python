
"""
The time complexity of the matrixMultStandard function can be analyzed by 
examining the nested loops in the code.

The outermost loop iterates n times, where n is the size of the matrices. 
The second loop also iterates n times, and the innermost loop iterates n 
times as well.

Since the innermost loop is nested within the second loop, and the second 
loop is nested within the outermost loop, the total number of iterations 
is n * n * n, which simplifies to n^3.

Therefore, the time complexity of the matrixMultStandard function is O(n^3), 
or cubic time complexity. This means that the execution time of the function 
increases significantly as the size of the matrices increases.
"""


# Define a function that performs standard matrix multiplication
def matrixMultStandard(A, B):
    """
    Performs standard matrix multiplication. 
    Assumes that the input matrices are power of 2.

    Args:
        A (list): The first matrix.
        B (list): The second matrix.

    Returns:
        list: The resulting matrix after multiplication.
    """
    n = len(A)  # Get the size of the matrices
    i = j = 0  # Initialize loop variables
    Z = [[0 for _ in range(n)] for _ in range(n)]  # Create an empty matrix to store the result

    # Perform matrix multiplication
    for i in range(n):  # Iterate over rows of matrix A
        for j in range(n):  # Iterate over columns of matrix B
            for k in range(n):  # Iterate over columns of matrix A and rows of matrix B
                Z[i][j] += A[i][k] * B[k][j]  # Multiply corresponding elements and add to the result matrix
    return Z  # Return the resulting matrix
