import math

S = 0

def height (x, sx):
    h = 2*sx/x
    return h

a = int(input())
b = int(input())
c = int(input())

p = (a + b + c)/2

S = math.sqrt(p*(p-a)*(p-b)*(p-c))

print(height(a, S))
print(height(b, S))
print(height(c, S))