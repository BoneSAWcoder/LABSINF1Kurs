import math as m

xy = []
xz = []
yz = []

lena = 0
lenb = 0
lenc = 0

#x1, y1 = 0, 0
#x2, y2 = 0, 5
#x3, y3 = 5, 0

x1 = int(input('x1 = '))
y1 = int(input('y1 = '))
x2 = int(input('x2 = '))
y2 = int(input('y2 = '))
x3 = int(input('x3 = '))
y3 = int(input('y3 = '))

x = [x1, y1]
y = [x2, y2]
z = [x3, y3]

def len_vec(a):
        len_vec = 0
        for i in a:
                len_vec += i**2
        return m.sqrt(m.fabs(len_vec))

#находим кординаты векторов
for i in range(2):
        xy.append(y[i] - x[i])
for i in range(2):
        xz.append(z[i] - x[i])
for i in range(2):
        yz.append(z[i] - y[i])

#находим длины векторов
lena = len_vec(xy)
lenb = len_vec(xz)
lenc = len_vec(yz)

P = lena + lenb + lenc

S = m.fabs((xz[0] - xy[0])*(yz[1] - xy[1]) - (yz[0] - xy[0])*(xz[1] - xy[1])) /2


#print(xy, xz, yz)
#print(lena, lenb, lenc)
print(P,S)