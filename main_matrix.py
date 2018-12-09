from playLA.Matrix import Matrix

if __name__ == '__main__':
    matrix = Matrix([[1,3,5],[2,4,6]])
    print(matrix)
    print(matrix.shape())
    print("row num = {}, col num = {}".format(matrix.row_num(), matrix.col_num()))
    print("matrix[0][0] = {}".format(matrix[0,0]))

    matrix2 = Matrix([[3,6,9],[1,4,7]])
    print("add: {}".format(matrix + matrix2))
    print("sub: {}".format(matrix - matrix2))
    print("{} * {} = {}".format(matrix2, 3, matrix2 * 3))
    print("{} * {} = {}".format(2, matrix2, 2 * matrix2))
    print("{}".format(-matrix2))
    print("{}".format(Matrix.zero(2, 2)))

    A = Matrix([[1,2], [3,4]])
    B = Matrix([[5,6], [7,8]])
    print("A.dot(B) = {}".format(A.dot(B)))
    print("B.dot(A) = {}".format(B.dot(A)))

    I = Matrix.identity(3)
    print("单位矩阵I = {}".format(I))
    print("matrix2.dot(I) = {}".format(matrix2.dot(I)))