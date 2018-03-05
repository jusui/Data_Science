# coding: utf-8
import pylab

if __name__ == '__main__':
    
    pylab.figure(0)
    pylab.plot([1,2,3,4], [1,7,3,5])

    pylab.figure(1)
    pylab.plot([1,2,3,4], [1,2,3,4])
    pylab.figure(2)
    pylab.plot([1,4,2,3], [5,6,7,8])
    pylab.savefig('Figure-Addie')
    pylab.figure(1)
    pylab.plot([5,6,10,3])
    pylab.savefig('Figure-Jane')

    # 11.1
    pylab.figure(3)
    principal = 10000 # 初期投資額
    interestRate = 0.05
    years = 20
    values = []
    for i in range(years + 1):
        values.append(principal)
        principal += principal * interestRate
    pylab.plot(values)

    
    
    pylab.show()
