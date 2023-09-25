
import matplotlib.pyplot as Grafiki
import random as Sluchaiynost
import numpy
import math

YList = []
for x in range(1,11):
    print(x)
    YList.append(math.sqrt(1 + math.exp(math.sqrt(x)) + math.cos(x**2))/math.fabs(1 - (math.sin(x))**3) + math.log(math.fabs(2*x)))
Grafiki.grid()
Grafiki.plot(range(1,6),YList[0:5:1], 'r.-')
Grafiki.scatter(range(6,11),YList[5:10:1])
Grafiki.show()