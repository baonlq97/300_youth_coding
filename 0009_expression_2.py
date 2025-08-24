from math import sqrt

a, b, c = map(int, input().split())

P = (21*(a*a) + 5*(b*b))/(2009*(c*c) + 15)
Q = sqrt((a*a) - 2*b)/(3*(c*c) + 4)
print("{:.4f} {:.4f}".format(P, Q))