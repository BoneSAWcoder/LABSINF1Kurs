import matplotlib.pyplot as plt
#A
x = float()
y = float()
Xdots = []
Ydots = []
for x in range(-50, 50):
    if x < 1:
        Xdots.append(x)
        y = x + 2
        Ydots.append(y)
    if x >= 1:
        Xdots.append(x)
        y = (x**2) - 6*x + 10
        Ydots.append(y)
plt.plot(Xdots, Ydots, 'g.-')
plt.show()
