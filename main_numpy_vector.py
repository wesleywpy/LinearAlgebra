import numpy as np

if __name__ == '__main__':
    print(np.__version__)
    vec1 = np.array([1,3,5])
    vec2 = np.array([2,5,7])
    print(vec1)
    print(vec2)

    # 创建
    print(np.zeros(5))
    print(np.ones(5))
    print(np.full(3, 23))