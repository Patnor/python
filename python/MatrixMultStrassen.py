
def addMatrices(A, B):
    n = len(A)
    C = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            C[i][j] = A[i][j] + B[i][j]
    return C


def matrixMultStrassen(A, B):
    n = len(A)

    if n <= 2:
            # Base case: if the matrices are 2x2, perform regular matrix multiplication
            if n == 2:
                C = [[0, 0], [0, 0]]
                C[0][0] = A[0][0] * B[0][0] + A[0][1] * B[1][0]
                C[0][1] = A[0][0] * B[0][1] + A[0][1] * B[1][1]
                C[1][0] = A[1][0] * B[0][0] + A[1][1] * B[1][0]
                C[1][1] = A[1][0] * B[0][1] + A[1][1] * B[1][1]
                return C

            # Recursive case: divide the matrices into submatrices
            else:
                # Divide matrices A and B into four submatrices
                mid = n // 2
                A11 = [A[i][:mid] for i in range(mid)]
                A12 = [A[i][mid:] for i in range(mid)]
                A21 = [A[i][:mid] for i in range(mid, n)]
                A22 = [A[i][mid:] for i in range(mid, n)]
                B11 = [B[i][:mid] for i in range(mid)]
                B12 = [B[i][mid:] for i in range(mid)]
                B21 = [B[i][:mid] for i in range(mid, n)]
                B22 = [B[i][mid:] for i in range(mid, n)]

                # Calculate the seven products required for Strassen's algorithm
                P1 = matrixMultStrassen(A11, subtractMatrices(B12, B22))
                P2 = matrixMultStrassen(addMatrices(A11, A12), B22)
                P3 = matrixMultStrassen(addMatrices(A21, A22), B11)
                P4 = matrixMultStrassen(A22, subtractMatrices(B21, B11))
                P5 = matrixMultStrassen(addMatrices(A11, A22), addMatrices(B11, B22))
                P6 = matrixMultStrassen(subtractMatrices(A12, A22), addMatrices(B21, B22))
                P7 = matrixMultStrassen(subtractMatrices(A11, A21), addMatrices(B11, B12))

                # Calculate the four quadrants of the resulting matrix C
                C11 = subtractMatrices(addMatrices(addMatrices(P5, P4), P6), P2)
                C12 = addMatrices(P1, P2)
                C21 = addMatrices(P3, P4)
                C22 = subtractMatrices(subtractMatrices(addMatrices(P5, P1), P3), P7)

                # Combine the four quadrants to form the resulting matrix C
                C = [[0] * n for _ in range(n)]
                for i in range(mid):
                    for j in range(mid):
                        C[i][j] = C11[i][j]
                        C[i][j + mid] = C12[i][j]
                        C[i + mid][j] = C21[i][j]
                        C[i + mid][j + mid] = C22[i][j]
                return C

