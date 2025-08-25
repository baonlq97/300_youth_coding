from math import sqrt

a, b, c = map(int, input().split())
perimeter = a + b + c
semi_perimeter = perimeter / 2
area = sqrt(semi_perimeter*(semi_perimeter - a)*(semi_perimeter - b)*(semi_perimeter - c))
print("{} {:.3f}".format(perimeter, area))