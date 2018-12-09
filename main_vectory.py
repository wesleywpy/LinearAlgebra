from playLA.Vector import Vector

if __name__ == '__main__':
    v1 = Vector([3, 5])
    print(v1.__len__())
    print(v1)

    v2 = Vector([1, 2])

    print("{} + {} = {}".format(v1, v2, v1 + v2))
    print("{} - {} = {}".format(v1, v2, v1 - v2))
    print("{} * {} = {}".format(3, v2, 3 * v2))
    print("{} * {} = {}".format(v1, 3, v1 * 3))
    print("+{} = {}".format(v1, +v1))
    print("-{} = {}".format(v2, -v1))

    v0 = Vector.zero(2)
    print(v0)

    print("norm({}) = {}".format(v1, v1.norm()))
    print("norm({}) = {}".format(v2, v2.norm()))
    print("norm({}) = {}".format(v0, v0.norm()))

    print("normalize({}) = {}".format(v1, v1.normalize()))
    print("normalize({}) = {}".format(v2, v2.normalize()))

    try:
        print("normalize({}) = {}".format(v0, v0.normalize()))
    except ZeroDivisionError:
        print("Cannot normalize zero Vector {}".format(v0))

    print(v1.dot(v2))