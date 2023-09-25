
import matplotlib.pyplot as Grafiki
import random as Sluchaiynost
import numpy

Randlist = []
XList = []
for i in range(Sluchaiynost.randint(10,50)):
    Randlist.append(Sluchaiynost.randint(0,1))
    XList.append(i)

Sred = sum(Randlist)/len(Randlist)
print(Sred)
Mid = numpy.median(Randlist)
print(Mid)

YList = [0,0]
for i in Randlist:
    if i == 0:
        YList[0] = YList[0] + 1
    if i == 1:
        YList[1] = YList[1] + 1

Grafiki.grid()
Grafiki.scatter([0,1], YList)
Grafiki.show()