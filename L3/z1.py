
def matrix_multiply(m_a, m_b):
    """
    Calculate the matrix dot product
    :param m_a: First matrix to multiply
    :param m_b: Second matrix to multiply
    :return: m_a & m_b dot product
    """
    # Check if the matrices are the same length and raise an error when they are not
    if len(m_a[0]) != len(m_b):
        raise ValueError("Number of columns in the first matrix must equal the number of rows in the second matrix.")

    # Init the output matrix
    result = [[0 for _ in range(len(m_b[0]))] for _ in range(len(m_a))]

    # Myltiply
    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                result[i][j] += m_a[i][k] * m_b[k][j]

    return result

a = [
    [1, 1, 1],
    [2, 2, 2],
    [3, 3, 3]
]

b = [
    [1, 1, 1],
    [2, 2, 2],
    [3, 3, 3]
]

print(matrix_multiply(a, b))

