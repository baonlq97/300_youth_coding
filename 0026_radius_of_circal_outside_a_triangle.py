from math import sqrt

a, b, c = map(int, input().split())
p = (a + b + c) / 2
S = sqrt(p * (p - a) * (p - b) * (p - c))
R = (a * b * c)/(4 * S)
print("{:.3f}".format(R))