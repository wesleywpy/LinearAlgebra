from .Matrix import Matrix
from .Vector import Vector
from ._global import is_zero

def lu(matrix):
    """方阵的LU分解"""
    assert matrix.row_num() == matrix.col_num(), "矩阵必须是方阵"

    n = matrix.row_num()
    # 矩阵的每一行
    A = [matrix.row_vector(i) for i in range(n)]
    # 构造一个单位矩阵
    L = [[1.0 if i == j else 0.0 for i in range(n)] for j in range(n)]

    for i in range(n):
        # A[i][i]位置是否是主元
        if is_zero(A[i][i]):
            return None, None
        else:
            for j in range(i+1, n):
                p = A[j][i] / A[i][i] # 主元所在列的其它值与主元之间的倍数
                A[j] = A[j] - p * A[i] #  其他列值为0
                L[j][i] = p

    return Matrix(L), Matrix([A[i].underlying_list() for i in range(n)])