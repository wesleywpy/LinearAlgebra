from .Vector import Vector

class Matrix:
    def __init__(self, list2d):
        self._values = [row[:] for row in list2d]

    @classmethod
    def zero(cls, r, c):
        """返回一个r行c列的零矩阵"""
        return cls([[0] * c for _ in range(r)])

    @classmethod
    def identity(cls, n):
        """返回一个n行n列的单位矩阵"""
        m = [[0] * n for _ in range(n)]
        for i in range(n):
            m[i][i] = 1
        return cls(m)

    def __add__(self, another):
        """返回两个矩阵的加法结果"""
        assert self.shape() == another.shape(), "加法计算错误, 矩阵的行与列必须相等"
        return Matrix([ [a + b for a, b in zip(self.row_vector(i), another.row_vector(i))]
                        for i in range(self.row_num())])

    def __sub__(self, another):
        """返回两个矩阵的减法结果"""
        assert self.shape() == another.shape(), "减法计算错误, 矩阵的行与列必须相等"
        return Matrix([ [a - b for a, b in zip(self.row_vector(i), another.row_vector(i))]
                        for i in range(self.row_num())])

    # range(5) 代表从0到5(不包含5)
    # 输出: [0, 1, 2, 3, 4]
    def __mul__(self, k):
        """数量乘法结果: self * k"""
        return Matrix([ [e * k for e in self._values[i]]
                        for i in range(self.row_num())])

    def __rmul__(self, k):
        """数量乘法: k * self"""
        return self * k

    def __truediv__(self, k):
        """返回数量除法的结果矩阵: self / k"""
        return (1 / k) * self

    def __pos__(self):
        """取正: +self"""
        return 1 * self

    def __neg__(self):
        """取负: -self"""
        return -1 * self

    def __getitem__(self, pos):
        """返回pos位置的元素"""
        r, c = pos
        return self._values[r][c]

    # 系统调用
    def __repr__(self):
        return "Matrix({})".format(self._values)

    __str__ = __repr__

    def dot(self, another):
        """矩阵乘法结果"""
        if isinstance(another, Vector):
            # 矩阵和向量的乘法
            assert self.col_num() == len(another), \
                "Error in Matrix-Vector Multiplication. 矩阵列数必须与向量元素个数相等"
            return Vector([self.row_vector(i).dot(another) for i in range(self.row_num())])

        if isinstance(another, Matrix):
            # 矩阵和矩阵的乘法
            assert self.col_num() == another.row_num(), \
                "Error in Matrix-Matrix Multiplication. "
            return Matrix([[self.row_vector(i).dot(another.col_vector(j)) for j in range(another.col_num())]
                           for i in range(self.row_num())])

    def row_vector(self, index):
        """返回矩阵第index行向量"""
        return Vector(self._values[index])

    def col_vector(self, index):
        """返回矩阵第index列向量"""
        return Vector([row[index] for row in self._values])

    def size(self):
        """返回矩阵的元素个数"""
        r, c = self.shape()
        return r * c

    def shape(self):
        """返回矩阵的形状: (行数, 列数)"""
        return len(self._values), len(self._values[0])

    def row_num(self):
        """返回矩阵的行数"""
        return self.shape()[0]

    def col_num(self):
        """返回矩阵的列数"""
        return self.shape()[1]
