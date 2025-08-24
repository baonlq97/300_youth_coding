a, b, c = map(int, input().split())

first = a // 2 + a % 2
second = b // 2 + b % 2
third = c // 2 + c % 2

total = first + second + third

print(total)