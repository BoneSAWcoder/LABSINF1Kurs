import matplotlib.pyplot as plt
#A
x = float()
y = float()
Xdots = []
Ydots = []
for x in range(-50, 50):
    Xdots.append(x)
    y = (x**2) - 1
    Ydots.append(y)
plt.plot(Xdots, Ydots, 'g.-')
#B
x = float()
y = float()
Xdots = []
Ydots = []
for x in range(-50, 50):
    Xdots.append(x)
    y = (x**2) - 8*x + 15
    Ydots.append(y)
plt.plot(Xdots, Ydots, 'r.-')
#C
x = float()
y = float()
Xdots = []
Ydots = []
for x in range(-50, 50):
    Xdots.append(x)
    y = (-2)*(x**2) + 4*x
    Ydots.append(y)
plt.plot(Xdots, Ydots, 'b.-')
plt.show()