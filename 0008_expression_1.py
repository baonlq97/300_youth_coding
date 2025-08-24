a = int(input())
b = int(input())

P = (21*a)  + (5*b) - 2009
Q = (21*(a*a) - 5*b)/(2009*(b*b))
R = (21*a + 5*(b*b)) / (2009*b + 15)
print("{} {:.4f}".format(P, Q))
print("{:.6f}".format(R))