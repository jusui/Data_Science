import numpy as np

def ndim():
    """
    check n dimension
    """

    a = np.array(100)
    print("a = np.array(100) =", a)
#    print(a.T)
    print("a.shape =", a.shape)
    
    b = np.array([10, 20, 30])
    print("b = np.array([10, 20, 30]) =", b)
#    print(b.T)
    print("b.shape =", b.shape)

    c = np.array([[1, 2, 3],[4, 5, 6]])
    print("c = np.array([[1, 2, 3], [4, 5, 6]]) =", c)
    print("c.shape =", c.shape)
    

if __name__ == '__main__':
    ndim()
    


    
