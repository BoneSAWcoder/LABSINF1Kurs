
import matplotlib.pyplot as Grafiki
import numpy
import math
import scipy.integrate

x = numpy.arange(0.0,10,1)
y = numpy.abs(numpy.fabs(numpy.cos(x*numpy.exp(numpy.cos(x) - numpy.log(x+1)))))

Grafiki.grid()
Grafiki.plot(x,y, c = 'r')
Grafiki.fill_between(x,y)
Grafiki.show()

area = numpy.trapz(y)
print(area)