import matplotlib.pyplot as plt
def MakeGraph(TextBarText, Xmin, Xmax):
    print(TextBarText)
    x = float()
    y = float() 
    Xdots = []
    Ydots = []
    for x in range(Xmin, Xmax):
        Xdots.append(x)
        y = eval(TextBarText)
        print(y)
        Ydots.append(y)
    plt.plot(Xdots, Ydots, 'b.-')
    plt.show()
