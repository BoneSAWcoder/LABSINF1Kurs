
class cube():
    a = 0
    Sparal = 0
    Ssurface = 0
    Vcube = 0
    def __init__(self, ConA):
        self.Sparal = ConA**2
        self.Ssurface = self.Sparal*6
        self.Vcube = ConA**3

CubeObj = cube(int(input()))
print(CubeObj.Sparal)
print(CubeObj.Ssurface)
print(CubeObj.Vcube)
