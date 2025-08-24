T, HS = map(int, input().split())

AVG = int(T/HS)
LEFT = T%HS

print("{} {}".format(AVG, LEFT))