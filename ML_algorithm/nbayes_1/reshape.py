import numpy as np

def reshape():
    """
    check reshape
    """

    a = np.arange(6)
    print("a =", a)

    b = np.reshape(np.arange(6), (2, 3))
    print("np.reshape(np.arnge(6), (2, 3)) =", b)

    c = np.arange(6).reshape((3, 2))
    print("np.arange(6).reshape(3, 2) =", c)

    d = np.arange(6).reshape((2, -1))
    print("np.arange(6).reshape((2, -1)) =", d)
    
    e = np.arange(6).reshape((1, -1))
    print("np.arange(6).reshape((1, -1)) =", e)

    f = np.arange(6).reshape((-1, 1))
    print("np.arange(6).reshape((-1, 1)) =", f)

    
if __name__ == '__main__':
    reshape()
           
