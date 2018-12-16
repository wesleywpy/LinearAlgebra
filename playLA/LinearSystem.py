from .Matrix import Matrix
from .Vector import Vector
from ._global import is_zero

class LinearSystem:

    def __init__(self, A, b):
        self._m = A.row_num()
        self._n = A.col_num()

        if isinstance(b, Vector):
            assert A.row_num() == len(b), "矩阵A行数必须等于向量b长度"
            # 每个向量表示一个线性方程
            self.Ab = [Vector(A.row_vector(i).underlying_list() + [b[i]]) for i in range(self._m)]

        if isinstance(b, Matrix):
            assert A.row_num() == b.row_num() and A.col_num() == b.col_num(), "增广矩阵行列数必须与矩阵A相等"
            self.Ab = [Vector(A.row_vector(i).underlying_list() + b.row_vector(i).underlying_list()) for i in range(self._m)]

        # 记录主元的位置
        self.pivots = []

    def gauss_jordan_elimination(self):
        """高斯-约旦 消元法, 有解返回True"""
        self._forward()
        self._backward()

        # 非零行 < 矩阵的行数
        for i in range(len(self.pivots), self._m):
            # 最后一列值 != 0
            if not is_zero(self.Ab[i][-1]):
                return False
        return True

    def _max_row(self, index_i, index_j, n):
        """
        :param index_i: 行
        :param index_j: 列
        :param n: 矩阵的总行数
        :return: 主元所处的最大行号
        """
        best, ret = self.Ab[index_i][index_j], index_i
        for i in range(index_i + 1, n):
            if self.Ab[i][index_j] > best:
                best, ret = self.Ab[i][index_j], i
        return ret

    def _forward(self):
        """前向过程"""
        i, k = 0, 0
        while i < self._m and k < self._n:
            # 当前位置 主元最大的行号
            max_row = self._max_row(i, k, self._m)
            # 主元所处最大行与当前行 交互位置
            self.Ab[i], self.Ab[max_row] = self.Ab[max_row], self.Ab[i]

            if is_zero(self.Ab[i][k]):
                k += 1
            else:
                # 除以当前位置元素的值 将主元归为1
                self.Ab[i] = self.Ab[i] / self.Ab[i][k]
                # 主元列的其它值归为0
                for j in range(i + 1, self._m):
                    self.Ab[j] = self.Ab[j] - self.Ab[j][k] * self.Ab[i]
                self.pivots.append(k)
                i += 1

    def _backward(self):
        """向后过程"""
        # 非零行的数量
        n = len(self.pivots)
        # 从后往前遍历, 步长为1
        for i in range(n - 1, -1, -1):
            # 主元的所处的lie Ab[i][k]为主元
            k = self.pivots[i]
            # 从后往前遍历, 主元列的其它值归为0
            for j in range(i - 1, -1, -1):
                self.Ab[j] = self.Ab[j] - self.Ab[j][k] * self.Ab[i]

    def fancy_print(self):
        for i in range(self._m):
            print(" ".join(str(self.Ab[i][j]) for j in range(self._n)), end= " ")
            print("|", self.Ab[i][-1])

def inv(A):
    """高斯消元法求矩阵的逆"""
    if A.row_num() != A.col_num():
        return None

    n = A.row_num()
    ls = LinearSystem(A, Matrix.identity(n))
    if not ls.gauss_jordan_elimination():
        return None

    # 取到高斯消元法之后的 增广矩阵 就是逆矩阵
    invA = [[row[i] for i in range(n, 2*n)] for row in ls.Ab]
    return Matrix(invA)