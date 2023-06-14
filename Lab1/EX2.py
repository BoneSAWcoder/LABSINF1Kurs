import math

class point:
    x = 0
    y = 0
    def __init__(self, ConstrX, ConstrY):
        self.x = ConstrX
        self.y = ConstrY
class vector:
    x = 0
    y = 0
    Lenght = 0
    def __init__(self, x1, x2, y1, y2):
        self.x = x2 - x1
        self.y = y2 - y1
        self.Lenght = math.sqrt(self.x**2 + self.y**2)    
class tasks:
    def __init__(self):
        pass
    def TriSpace(x1, x2, y1, y2):
        Space = (x1 * y2) - (y1 * x2)
        return Space
    def Perimeter(a, b, c):
        lenght = a + b + c
        return lenght

A = point(int(input()), int(input()))
B = point(int(input()), int(input()))
C = point(int(input()), int(input()))

AB = vector(A.x, B.x, A.y, B.y)
AC = vector(A.x, C.x, A.y, C.y)
CB = vector(C.x, B.x, C.y, B.y)

Task = tasks()
print(tasks.Perimeter(AB.Lenght, AC.Lenght, CB.Lenght))
print(tasks.TriSpace(AB.x, AC.x, AB.y, AC.y))