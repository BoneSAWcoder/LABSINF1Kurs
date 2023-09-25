x = [0,1,2,3,4,5,6,7,8,9]
b1 = x[::2]
b2 = b1[::-1]
a = x[1:10:2]
print(b2)
print(a)
c = []
for i in range(int(len(x)//2)):
    c.append(b2[i])
    c.append(a[i])
print(c)