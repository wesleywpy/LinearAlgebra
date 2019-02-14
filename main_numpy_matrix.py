import numpy as np

if __name__ == '__main__':
    # 矩阵的创建
    A = np.array([[1,2], [3, 4]])

    print(A)

    # 矩阵的属性

    # 获取矩阵的元素

    # : 切片表达式, 表示从头到尾
    print(A[:,0])

    # 单位矩阵
    I = np.identity(2)
    print(A.dot(I))
    print("I.dot(A) = {}".format(I.dot(A)))

    # 逆矩阵
    invA = np.linalg.inv(A)
    print(invA)
    print(invA.dot(A))

    B = np.array([[1,4,2], [0, 3, 0], [6, 7, 5]])
    C = np.array([[1,4,6], [0, 2, 5], [0, 1, 3]])
    print(B.dot(C))

    # 对角矩阵
    print(np.eye(4,3))
