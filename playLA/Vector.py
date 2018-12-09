from ._global import is_zero
import math


class Vector:

    def __init__(self, lst):
        self._values = list(lst)

    # 类方法
    @classmethod
    def zero(cls, dim):
        """返回一个dim维度的零向量"""
        return cls([0] * dim)

    def norm(self):
        """返回向量的模"""
        return math.sqrt(sum(e ** 2 for e in self))

    def normalize(self):
        """返回向量的单位向量"""
        # 浮点运算0比较存在精度丢失情况,所以采用比较大小
        if is_zero(self.norm()):
            raise ZeroDivisionError("Normalize error! norm is zero.")
        # return 1 / self.norm() * Vector(self._values)
        return Vector(self._values) / self.norm()

    def  dot(self, another):
        """向量点乘, 返回结果标量"""
        assert len(self) == len(another), "Error in Dot Product, Length of vectors must be same"
        return sum(a * b for a, b in zip(self, another))

    def underlying_list(self):
        """返回向量元素"""
        return self._values

    def __add__(self, another):
        """向量加法, 返回结果向量"""
        # python assert断言是声明其布尔值必须为真的判定，如果发生异常就说明表达示为假。
        assert len(self) == len(another), "加法计算错误, 向量维度必须一致"
        return Vector([a + b for a, b in zip(self, another)])

    def __sub__(self, another):
        """向量减法, 返回结果向量"""
        assert len(self) == len(another), "减法计算错误, 向量维度必须一致"
        return Vector([a - b for a, b in zip(self, another)])

    def __mul__(self, k):
        """向量数量乘法, 返回结果向量"""
        return Vector([k * e for e in self])

    def __rmul__(self, k):
        return self * k

    # 除法运算符重载
    def __truediv__(self, k):
        """返回数量除法的结果向量 self / k"""
        return 1 / k * self

    def __pos__(self):
        """返回向量取正的结果向量"""
        return 1 * self

    def __neg__(self):
        """返回向量取负的结果向量"""
        return -1 * self

    def __getitem__(self, index):
        """返回向量的第index个元素"""
        return self._values[index]

    def __iter__(self):
        """向量迭代器"""
        return self._values.__iter__()

    def __len__(self):
        """
        :return: 向量的维度
        """
        return len(self._values)

    # 系统调用
    def __repr__(self):
        return "Vector({})".format(self._values)

    # 用户调用
    def __str__(self):
        return "({})".format(", ".join(str(e) for e in self._values))