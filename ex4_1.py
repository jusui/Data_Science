# -*- encoding utf-8 -*-
"""
This script is encoding test

"""

import math

def myfun(x, y):
    """ My function """

    a = math.cos(3 * (x - 1)) + \
        math.sin(3 * (y - 1))
    return a


# __* : Def in this system
if __name__ == '__main__':
    # Use myfun
    x, y = 2.0, 5.0
    print("myfun(x,y) = %f" % myfun(x,y) )
    
    
