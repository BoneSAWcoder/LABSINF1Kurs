
import matplotlib.pyplot as Grafiki
import numpy
import math
import scipy.integrate

print('1)+\n','2)-\n','3)*\n','4)/\n','5)e^(x+y)\n','6)sin(x+y)\n','7)cos(x+y)\n','8)x^y\n')
Ch = int(input('Choose operation: '))
x = int(input('X: '))
y = int(input('Y: '))

match Ch:
    case 1:
        print(x+y)
    case 2:
        print(x-y)
    case 3:
        print(x*y)
    case 4:
        print(x/y)
    case 5:
        print(math.exp(x+y))
    case 6:
        print(math.sin(x+y))
    case 7:
        print(math.cos(x+y))
    case 8:
        print(x**y)