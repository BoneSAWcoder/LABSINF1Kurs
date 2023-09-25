
x = int(input())
if x < -5:
    print('c in [-inf, -5]')
elif x >= -5 and x <= 5:
    print('c in [-5, 5]')
elif x > 5:
    print('c in [5, +inf]')