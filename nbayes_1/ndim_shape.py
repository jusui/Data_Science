import numpy as np

def ndim_shape():
    """
    check n dimension
    """

    a = np.array( [[1, 3], [2, 1]] )
    print("a =", a)
    print("a.T =", a.T)
    print("a.transpose() =", a.transpose())

    print("Let's transpose 1-d array")
    b = np.array([10, 20])
    print("b =", b)
    print("b.T =", b.T)    

    print("b =", b)
    print("b.ndim =", b.ndim)
    print("b.shape =", b.shape) 
    
    c = b[:, np.newaxis]
    print("c = b[:, np.newaxis] =", c)
    print("c.ndim =", c.ndim)
    print("c.shape =", c.shape)

    d = b[np.newaxis, :]
    print("d = b[np.newaxis, :] =", d)
    print("d.ndim =", d.ndim)
    print("d.shape =", d.shape)

    print("c.T =", c.T)
    print("d.T =", d.T)

    e = np.array([[1, 2, 3], [2, 4, 6]])
    print("e.shape =", e.shape)
    print("e[np.newaxis, :, :].shape =", e[np.newaxis, :, :].shape)
    print("e[:, np.newaxis, :].shape =", e[:, np.newaxis, :].shape)
    print("e[:, :, np.newaxis].shape =", e[:, :, np.newaxis].shape)
    print("e[np.newaxis, :, np.newaxis, :].shape =", e[np.newaxis, :, np.newaxis, :].shape)
   

if __name__ == '__main__':
    ndim_shape()
    


    
