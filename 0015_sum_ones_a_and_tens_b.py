a, b = map(int, input().split())

ones_a = a % 10
tens_b = (b // 10) % 10

sum = ones_a + tens_b
print(sum)