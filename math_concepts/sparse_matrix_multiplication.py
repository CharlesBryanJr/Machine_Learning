'''sparse_matrix_multiplication'''
# pylint: disable=C0114
# pylint: disable=E1101
# pylint: disable=C0103
# pylint: disable=E1101
# pylint: disable=C0116
# pylint: disable=C0115
# pylint: disable=W0105
# pylint: disable=C0304
# pylint: disable=W0621
print(" ")

'''

Type of Question:
- 

Clarifying Questions / Insights:
- both matrices will be sparse
- sparse == most of their elements will be zero
- given sparse matrices, reduce the number of computations.

Question:
Write a function that takes in 
two integers matrices 
and
multiples them together.
-

Input:
- Intuitive
- Primitive Types
		- Numbers
			- Zero (0)
			- NULL or nil
			- Negative Numbers
			- Floats or Doubles (clarifies if Ints only?)
			- Min/Max Int
		- Arrays
			- Empty array
			- Nested or not nested
	
- If I knew / had this....
	- Dictionary of Keys

Output: matrix
- [[]]
'''

# Time: O() | # Space: O()
def sparse_matrix_multiplication_1(matrix_a, matrix_b):

    # Verify if columns of A == rows of B
    if len(matrix_a[0]) != len(matrix_b):
        return [[]]

    # Pre-calculate the dimensions
    rows_a = len(matrix_a)
    cols_a = len(matrix_a[0])
    cols_b = len(matrix_b[0])

    # create matrix c, initalize with zeros
    matrix_c = [[0] * cols_b for _ in range(rows_a)]

    # perform matrix multiplication and update matrix c
    for i in range(rows_a):
        for j in range(cols_b):
            for k in range(cols_a):
                matrix_c[i][j] += matrix_a[i][k] * matrix_b[k][j]

    return matrix_c

def sparse_matrix_multiplication_2(matrix_a, matrix_b):
    if len(matrix_a[0]) != len(matrix_b):
        return [[]]

    rows_a = len(matrix_a)
    cols_a = len(matrix_a[0])
    cols_b = len(matrix_b[0])

    matrix_c = [[0] * cols_b for _ in range(rows_a)]

    for i in range(rows_a):
        for k in range(cols_a):
            if matrix_a[i][k] != 0:
                for j in range(cols_b):
                    matrix_c[i][j] += matrix_a[i][k] * matrix_b[k][j]

    return matrix_c

def sparse_matrix_multiplication(matrix_a, matrix_b):
    rows_a = len(matrix_a)
    cols_a = len(matrix_a[0])
    rows_b = len(matrix_b)
    cols_b = len(matrix_b[0])

    if cols_a != rows_b:
        return [[]]

    sparse_a = get_dict_of_nonzero_cells(matrix_a)
    sparse_b = get_dict_of_nonzero_cells(matrix_b)

    matrix_c = [[0] * cols_b for _ in range(rows_a)]

    for row_a, col_a in sparse_a:
        for row_b, col_b in sparse_b:
            is_compatible_position = (col_a == row_b)
            if is_compatible_position:
                matrix_c[row_a][col_b] += sparse_a[(row_a, col_a)] * sparse_b[(row_b, col_b)]

    return matrix_c


def get_dict_of_nonzero_cells(matrix):
    dict_of_nonzero_cells = {}

    for i, row in enumerate(matrix):
        for j, value in enumerate(row):
            if value != 0:
                dict_of_nonzero_cells[(i, j)] = value

    return dict_of_nonzero_cells



matrix_a = [
    [0, 2, 0],
    [0, -3, 5]
]
matrix_b = [
    [0, 10, 0],
    [0, 0, 0],
    [0, 0, 4]
]
print("matrix_a:", matrix_a)
print("matrix_b:", matrix_b)
print("sparse_matrix_multiplication_1:", sparse_matrix_multiplication_1(matrix_a, matrix_b))
print("sparse_matrix_multiplication_2:", sparse_matrix_multiplication_2(matrix_a, matrix_b))
print("sparse_matrix_multiplication:", sparse_matrix_multiplication(matrix_a, matrix_b))
print(" ")

matrix_a = [
    [0],
    [0],
    [0],
    [0],
    [0],
    [3],
    [0],
    [0]
]
matrix_b = [
    [0, 0, 0, 0, 0, 2, 0, 0]
]
print("matrix_a:", matrix_a)
print("matrix_b:", matrix_b)
print("sparse_matrix_multiplication_1:", sparse_matrix_multiplication_1(matrix_a, matrix_b))
print("sparse_matrix_multiplication_2:", sparse_matrix_multiplication_2(matrix_a, matrix_b))
print("sparse_matrix_multiplication:", sparse_matrix_multiplication(matrix_a, matrix_b))
print(" ")

matrix_a = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [-5, -9, 0, 0, 7, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 5, -4, -3, 0],
    [0, 0, 0, 0, 0, 0, 0, -2, 0, 0, 0, 0],
    [0, 0, -8, 0, 0, 0, 0, 0, 0, 0, 6, 0],
    [0, 0, 0, 0, 9, 0, 3, 4, 0, 0, 0, 0]
]
matrix_b = [
    [3, 0],
    [0, 0],
    [8, 0],
    [7, 0],
    [-8, 0],
    [0, 0],
    [0, 0],
    [0, 0],
    [0, 8],
    [0, 0],
    [0, 0],
    [0, 0]
]
print("matrix_a:", matrix_a)
print("matrix_b:", matrix_b)
print("sparse_matrix_multiplication_1:", sparse_matrix_multiplication_1(matrix_a, matrix_b))
print("sparse_matrix_multiplication_2:", sparse_matrix_multiplication_2(matrix_a, matrix_b))
print("sparse_matrix_multiplication:", sparse_matrix_multiplication(matrix_a, matrix_b))
print(" ")

# _recursion
# _iteration
print(" ")
