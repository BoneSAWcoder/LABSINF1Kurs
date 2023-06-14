import math as m

def print1 (a,b):
    print(a)
    print(b)

x = float(input('x = '))
y = float(input('y = '))
z = float(input('z = '))

#а
a = (m.sqrt(m.fabs(x-1)) - m.pow(m.fabs(y), (1/3))) / (1 + ((x*x) / 2) + (y*y) / 4)
b = x * (m.atan(z) + m.exp(-(x+3)))

print('а')
print1(a,b)

#г
a = y + x / (y*y + m.fabs(x*x / (y + (x**3)/3)))
b = 1 + m.tan(z/2)**2

print('\nг')
print1(a,b)

#ж
a = m.log(m.fabs((y - m.sqrt(m.fabs(x))) * (x - y/(z + x**2/4))))
b = x - x*x / m.factorial(3) + x**5 / m.factorial(5)

print('\nж')
print1(a,b)